FROM nginx:1.25.2

HEALTHCHECK CMD curl --fail http://localhost:80 || exit 1

LABEL testing-service="Mocking Fronius Inverter"
USER  nginx

COPY GetPowerFlowRealtimeData.fcgi /usr/share/nginx/html/GetPowerFlowRealtimeData.fcgi

