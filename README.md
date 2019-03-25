# Data Transformation Module <br />
Data Transformation allows you to apply normalization or z-score to the values in your data list <br />

## What is Normalization <br />
**Normalization** Min-max normalization method is applied to convert data between 0 and 1 numerical values
<br />
**Normalization** formula is given below<br />
![Min-Max Normalization's Formula](https://qph.fs.quoracdn.net/main-qimg-0d692d88876aeb26b1f1a578d1c5a94e.webp) <br />

## What is Z-Score <br />
**Z-Score**     This method is based on converting data into new values, taking into account the mean and standard errors.<br />
**Z-Score** formula is given below<br />
![Z-Score's Formula](https://www.statisticshowto.datasciencecentral.com/wp-content/uploads/2014/02/z-score.png) <br />

# Basic Statistic Module <br />
Basic statistical operations, mean finding and standard deviation is the module that performs the process <br />

## What is Avarage(Arithmetic Mean) <br />
The statistical method we find by dividing the sum of the numbers in a list by the number of elements of the list <br />

**Avarage(Arithmetic Mean)** formula is given below <br />
![Avarage's Formula](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjySwjrEz0s92rdm0JuZGXINSWrLtpoRgXKR8hM6v8fjIo5hUj)<br />

## What is Standard Deviation <br />
The statistical method we find by dividing the sum of the numbers in a list by the number of elements of the list <br />

**Standard Deviation** formula is given below <br />
![Standard Deviation's Formula](https://s3-eu-west-1.amazonaws.com/tutor2u-media/subjects/psychology/studynote-images/standard-deviation-formula.png?mtime=20151126161915)<br />

## How Can I Use? <br />
>import DataTransformation<br />
>numericList = [30,36,45,50,62] <br />
>print("Normalization: ",DataTransformation.normalization(numericList))<br />
>print("zScore: ",DataTransformation.zScore(numericList))<br />
