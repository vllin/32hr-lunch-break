cod <- read.csv(file = './NCHS_-_Leading_Causes_of_Death__United_States.csv', header = TRUE, sep = ',')
suicides16 <- cod[(cod$Cause.Name == 'Suicide') & (nc_cod$Year == 2016),]
