import os
import csv
import SimpleITK as sitk
from radiomics import featureextractor

class Processing:
    def __init__(self, csv_file, resampled_mask_output_dir):
        self.csv_file = csv_file
        self.resampled_mask_output_dir = resampled_mask_output_dir
        self.extractor = featureextractor.RadiomicsFeatureExtractor()

    def resample_mask_to_image(self, mask, image, output_mask_path):
        try:
            resampler = sitk.ResampleImageFilter()
            resampler.SetReferenceImage(image)
            resampler.SetInterpolator(sitk.sitkNearestNeighbor)
            resampler.SetOutputDirection(image.GetDirection())
            resampler.SetOutputSpacing(image.GetSpacing())
            resampler.SetSize(image.GetSize())
            resampler.SetOutputOrigin(image.GetOrigin())

            resampled_mask = resampler.Execute(mask)
            sitk.WriteImage(resampled_mask, output_mask_path)
            print(f"Masque redimensionné sauvegardé à : {output_mask_path}")

            return resampled_mask
        except Exception as e:
            print(f"Erreur lors du rééchantillonnage du masque : {e}")

    def extract_radiomics_features(self, categories=None):
        results = []
        data_dir = "data"  # Dossier où les masques rééchantillonnés seront sauvegardés

        with open(self.csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                image_path = row['Image']
                mask_path = row['Mask']

                if os.path.exists(image_path) and os.path.exists(mask_path):
                    try:
                        # Charger l'image et le masque
                        image = sitk.ReadImage(image_path)
                        mask = sitk.ReadImage(mask_path)

                        # Créer le chemin pour le masque rééchantillonné
                        mask_filename = os.path.basename(mask_path)
                        output_mask_path = os.path.join(data_dir, f"resampled_{mask_filename}")

                        # Vérifier si les tailles correspondent, sinon rééchantillonner le masque
                        if image.GetSize() != mask.GetSize():
                            print(f"Redimensionnement du masque pour qu'il corresponde à l'image : {image_path}")
                            mask = self.resample_mask_to_image(mask, image, output_mask_path)
                        else:
                            print(f"Pas de redimensionnement nécessaire pour : {image_path}")

                        # Extraire les caractéristiques radiomiques
                        extraction_result = self.extractor.execute(image, mask)

                        # Filtrer les résultats selon les catégories si spécifié
                        if categories:
                            filtered_result = {key: value for key, value in extraction_result.items() if any(cat in key for cat in categories)}
                        else:
                            filtered_result = extraction_result

                        # Ajouter les chemins de l'image et du masque aux résultats
                        filtered_result.update({'Image': image_path, 'Mask': mask_path})
                        results.append(filtered_result)

                        print("Extraction terminée pour:", image_path)

                    except Exception as e:
                        print(f"Erreur lors du traitement de {image_path}: {e}")
                else:
                    print(f"Fichiers non trouvés : {image_path} ou {mask_path}")

        return results
