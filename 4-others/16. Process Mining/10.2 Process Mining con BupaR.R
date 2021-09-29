#################################################################################
cat("\014")
#################################################################################

# Borrar Environment y consola y establecer working directory

rm(list = ls())

#################################################################################
### CARGAR LIBRERÍAS
#################################################################################

# install.packages("bupaR")
# install.packages("edeaR")
# install.packages("eventdataR")
# install.packages("processmapR")
# install.packages("processmonitR")
# install.packages("xesreadR")
# install.packages("petrinetR")

library(bupaR)
# library(dplyr)

#################################################################################
### LEER LOG 
### TRANSFORMAR Y CONVERTIR A OBJETO BUPAR
#################################################################################

eventlog <- patients

sample <- eventlog %>% 
  arrange(patient, time, handling)

sample %>% head(n = 50) %>% print.data.frame()

#################################################################################
### ESTADÍSTICA BÁSICA
#################################################################################

summary(eventlog)
activities(eventlog)
cases(eventlog)
resources(eventlog)
traces(eventlog)

mapping(eventlog)
activity_id(eventlog)
activity_instance_id(eventlog)
case_id(eventlog)
lifecycle_id(eventlog)
resource_id(eventlog)
timestamp(eventlog)

n_activities(eventlog)
n_activity_instances(eventlog)
n_cases(eventlog)
n_events(eventlog)
n_resources(eventlog)
n_traces(eventlog)

#################################################################################
### ANÁLISIS EXPLORATORIO Y DESCRIPTIVO
#################################################################################

eventlog %>% activity_frequency(level = 'activity') %>% plot()
eventlog %>% trace_length(level = 'trace') %>% plot()

#################################################################################
### TRACE EXPLORER
#################################################################################

eventlog %>% group_by_case() %>% trace_explorer(cov = 1, type = 'frequent')

#################################################################################
### DOTTED CHARTS ACTIVIDADES
#################################################################################

eventlog %>% dotted_chart(x='absolute', sort='start', color='handling')
eventlog %>% dotted_chart(x='relative', sort='duration', units='days', 
                          color='handling')

# eventlog %>% idotted_chart()

#################################################################################
### DOTTED CHARTS RECURSOS
#################################################################################

eventlog %>% dotted_chart(x='absolute', sort='start', color='employee')
eventlog %>% dotted_chart(x='relative', sort='duration', units='days', 
                          color='employee')

#################################################################################
### VISUALIZACIONES DEL PROCESO
### PROCESO COMPLETO
#################################################################################

eventlog %>% process_map(type=frequency('absolute'))
eventlog %>% process_map(type=frequency('relative'))
eventlog %>% process_map(performance(mean, 'hours'))

#################################################################################
### TIEMPOS DE PROCESAMIENTO
#################################################################################

eventlog %>% processing_time('activity') %>% plot
eventlog %>% throughput_time('log') %>% plot

#################################################################################
### PARTICIPACIÓN DE RECURSOS
#################################################################################

eventlog %>% resource_involvement('resource') %>% plot

#################################################################################
### MATRIZ DE PRECEDENCIAS
#################################################################################

eventlog %>% precedence_matrix(type = 'absolute') %>% plot
eventlog %>% precedence_matrix(type = 'relative') %>% plot

#################################################################################
### MAPA DE RECURSOS
#################################################################################

eventlog %>% resource_map()



