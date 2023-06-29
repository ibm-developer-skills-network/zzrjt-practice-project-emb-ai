APP_NAME="sentiment-analysis-nlp-bert"
CONTAINER_IMAGE_URL="us.icr.io/sn-labsassets/sentiment-bert-watson-nlp-runtime"
VISIBILITY=project
ibmcloud ce application create \
--name ${APP_NAME} \
--env ACCEPT_LICENSE=true \
--image ${CONTAINER_IMAGE_URL} \
--registry-secret icr-secret \
--visibility ${VISIBILITY}
