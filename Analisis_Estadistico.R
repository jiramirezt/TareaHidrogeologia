# Cargar libreria de estudio
library(FactoMineR)
library(psych)

datos_anaq <- read.csv("analisis_estadistico.csv", header=TRUE, sep = ",")
summary(datos_anaq)

datos_filtro <- datos_anaq[, c(4:17)]
df_describ <- describe(datos_filtro)
write.table(df_describ, row.names = T, col.names = T, file=paste("Datos_Resume2.csv"), sep = ",")

# Filtrado de elementos activos
res <- PCA(datos_filtro, quanti.sup = c(12,13), ncp = Inf)
res$eig
res <- PCA(datos_filtro, quanti.sup = c(12,13), ncp = 8)

res.hcpc <- HCPC(res, kk=Inf, min= 3, max=10, consol=TRUE)