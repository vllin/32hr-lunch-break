alc <- read.csv(file = './alcohol.csv', header = TRUE, sep = ',')

init_binging <- alc[alc$Question == 'Binge drinking intensity among adults aged >= 18 years who binge drink',]
init_consumption <- alc[alc$Question == 'Per capita alcohol consumption among persons aged >= 14 years',]

states <- read.csv(file = './states.csv', header = TRUE, sep = ',')$State

binging = rep(0,50)
names(binging) <- states
binging_vals <- data.frame(init_binging$DataValue)
binging_vals[is.na(binging_vals)] <- 0
for (j in states){
  for (i in 1:length(init_binging$LocationAbbr)){
    if (init_binging$LocationDesc[i] == j){
      binging[j] = binging[j] + binging_vals[[1]][i]
    }
  }
}

consumption = rep(0,50)
names(consumption) <- states
for (j in states){
  for (i in 1:length(init_consumption$LocationAbbr)){
    if (init_consumption$LocationDesc[i] == j){
      consumption[j] = consumption[j] + init_consumption$DataValue[i]
    }
  }
}

write.csv(binging, file = './binging.csv')
write.csv(consumption, file = './consumption.csv')