set -e
source .env

gcloud builds submit --pack image=gcr.io/${PROJECT_ID}/myimage
gcloud builds submit --config migrate.yaml
gcloud run deploy django-cloudrun \
  --platform managed \
  --region $REGION \
  --image gcr.io/${PROJECT_ID}/myimage \
  --set-cloudsql-instances ${PROJECT_ID}:${REGION}:myinstance \
  --set-secrets APPLICATION_SETTINGS=application_settings:latest \
  --service-account $SERVICE_ACCOUNT \
  --allow-unauthenticated

gcloud run services update django-cloudrun \
  --platform managed \
  --region $REGION \
  --image gcr.io/${PROJECT_ID}/myimage