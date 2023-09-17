FROM nginx:mainline-alpine3.18-slim

LABEL testing-service="Mocking Fronius Inverter"
# USER  nginx

COPY GetPowerFlowRealtimeData.fcgi /usr/share/nginx/html/GetPowerFlowRealtimeData.fcgi
# HEALTHCHECK CMD curl --fail http://localhost:8080 || exit 1
