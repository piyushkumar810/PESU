@echo off
REM =========================================================================
REM Build and Deploy Script for PersonForm on Apache Tomcat 9
REM Environment: Java JDK 20 + Apache Tomcat 9.0
REM =========================================================================

echo [1/4] Setting environment paths...
set "TOMCAT_DIR=C:\Program Files\Apache Software Foundation\Tomcat 9.0"
set "SERVLET_JAR=%TOMCAT_DIR%\lib\servlet-api.jar"

if not exist "%SERVLET_JAR%" (
    echo ERROR: Cannot find servlet-api.jar at: "%SERVLET_JAR%"
    echo Please verify your Tomcat installation path.
    pause
    exit /b 1
)

echo [2/4] Compiling Java classes with javac...
if not exist "target\classes" mkdir "target\classes"
javac -cp "%SERVLET_JAR%" -d "target\classes" src\main\java\com\example\Person.java src\main\java\com\example\PersonServlet.java src\main\java\com\example\SerializationDemo.java

if %ERRORLEVEL% neq 0 (
    echo ERROR: Java compilation failed!
    pause
    exit /b %ERRORLEVEL%
)

echo [3/4] Packaging PersonForm.war...
if exist "target\staging" rmdir /s /q "target\staging"
mkdir "target\staging\WEB-INF\classes"
xcopy /s /e /y "target\classes\*" "target\staging\WEB-INF\classes\" >nul
xcopy /s /e /y "src\main\webapp\*" "target\staging\" >nul

cd target\staging
jar -cvf "..\PersonForm.war" * >nul
cd ..\..

echo [4/4] Deploying to Tomcat webapps...
if exist "%TOMCAT_DIR%\webapps" (
    copy /y "target\PersonForm.war" "%TOMCAT_DIR%\webapps\PersonForm.war"
    echo.
    echo =========================================================================
    echo BUILD AND DEPLOYMENT SUCCESSFUL!
    echo.
    echo 1. Start Tomcat from Tomcat Service Manager or bin\startup.bat
    echo 2. Open your browser and navigate to:
    echo    http://localhost:8050/PersonForm/
    echo =========================================================================
) else (
    echo Note: PersonForm.war generated at target\PersonForm.war.
    echo Copy it manually to your Tomcat webapps folder if running as Admin.
)

pause
