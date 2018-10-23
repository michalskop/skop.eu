
library("Zelig")
library("ZeligEI")
sink()
sink("/dev/null")   # Suppress output after command or script run in R console

ncalc = 5  # number of repetitions of the calculcations (to get better means)
mats = list()

data = read.csv(par_input, header = TRUE, fileEncoding = "utf-8", encoding = "utf-8")
variables = names(data)
As = variables[which(grepl("A", variables) == TRUE)]
Bs = variables[which(grepl("B", variables) == TRUE)]

for (i in 1:ncalc) {
    z.out = zeirxc$new()
    eval(parse(text = paste0( "z.out$zelig(cbind(" , paste(Bs, collapse = ", "), ") ~ cbind(", paste(As, collapse = ", "), "), N='ZeligN', data = data)")))
    mat = matrix(apply(as.matrix(z.out$getcoef()[[1]][[3]]),2,'mean'),ncol=length(Bs))
    mats[[i]] = mat
}

# z.out$zelig(cbind(K2_2, K2_7, K2_9) ~ cbind(K1_1, K1_2, K1_3, K1_4, K1_5, K1_6, K1_7, K1_8, K1_9), N="ZeligN", data = data)
# eval(parse(text = paste0("z.out <- zelig(cbind(", paste(parties2016, collapse = ", "), ") ~ ", paste(parties2012, collapse = " + "), ", covar = NULL, model = 'ei.RxC', data = data)")))

matsd = matrix(apply(as.matrix(z.out$getcoef()[[1]][[3]]),2,'sd'),ncol=length(Bs))

mat_ave = apply(simplify2array(mats),1:2,mean)
matp = mat_ave / apply(mat_ave,1,'sum')

sink()

z.out = zeirxc$new()

#matp = mat / apply(mat,1,'sum')
