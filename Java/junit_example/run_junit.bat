:: put junit-4.12 and hamcrest-core-1.3 under .
:: this batch script takes one param as test file name

:: acquire test file name (without .java) using %1 parameter
:: execute commands
javac -cp .;junit-4.12.jar;hamcrest-core-1.3.jar %1.java
java -cp .;junit-4.12.jar;hamcrest-core-1.3.jar org.junit.runner.JUnitCore %1