# Usage PWD='' DNS_NAME='' NAMESPACE='' sh gen_cert.sh

DNS_NAME=${DNS_NAME:-elasticsearch-master}
NAMESPACE=${NAMESPACE:-adata}
PWD=${PWD:-'m9oxl3nm5ued3j3hps03'}

docker run --name elastic-helm-charts-certs -i -w /app \
		elasticsearch:7.12.1 \
		/bin/sh -c " \
			elasticsearch-certutil ca --out /app/elastic-stack-ca.p12 --pass '' && \
			elasticsearch-certutil cert --name ${DNS_NAME} --dns ${DNS_NAME} --ca /app/elastic-stack-ca.p12 --pass '' --ca-pass '' --out /app/elastic-certificates.p12" && \
docker cp elastic-helm-charts-certs:/app/elastic-certificates.p12 ./ && \
docker rm -f elastic-helm-charts-certs && \
openssl pkcs12 -nodes -passin pass:'' -in elastic-certificates.p12 -out elastic-certificate.pem && \
kubectl create -n ${NAMESPACE} secret generic elastic-certificate-pem --from-file=elastic-certificate.pem && \
kubectl create -n ${NAMESPACE} secret generic elastic-certificates --from-file=elastic-certificates.p12 && \
kubectl create -n ${NAMESPACE} secret generic elastic-credentials --from-literal=password=${PWD} --from-literal=username=elastic && \
rm -f elastic-certificates.p12
