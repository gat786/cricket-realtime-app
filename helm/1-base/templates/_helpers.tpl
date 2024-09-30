{{/*
Expand the name of the chart.
*/}}
{{- define "realtime-app-chart.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "realtime-app-chart.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "realtime-app-chart.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "realtime-app-chart.labels" -}}
helm.sh/chart: {{ include "realtime-app-chart.chart" . }}
{{ include "realtime-app-chart.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "realtime-app-chart.selectorLabels" -}}
app.kubernetes.io/name: {{ include "realtime-app-chart.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "realtime-app-chart.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "realtime-app-chart.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}


{{- define "frontend.labels" -}}
app: frontend
{{- end }}

{{- define "frontend.env" -}}
env:
  - name: Urls__Players
    value: http://{{ .Values.playerService.service.name }}.{{ .Release.Namespace }}.svc
  - name: Urls__Teams
    value: http://{{ .Values.teamService.service.name }}.{{ .Release.Namespace }}.svc
  - name: Urls__Score
    value: http://{{ .Values.scoreService.service.name }}.{{ .Release.Namespace }}.svc
  - name: Urls__ScoreWebsocket
    value: ws://{{ .Values.scoreService.service.name }}.{{ .Release.Namespace }}.svc
{{- end }}

{{- define "scoreService.labels" -}}
app: score-service
{{- end }}

{{- define "playerService.labels" -}}
app: player-service
{{- end }}

{{- define "teamService.labels" -}}
app: team-service
{{- end }}
