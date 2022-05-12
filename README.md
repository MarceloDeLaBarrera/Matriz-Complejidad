# Matriz-Complejidad

## Tabla de contenidos

- [Empezando](#Empezando-)
- [Screenshot](#Screenshot-)
- [Requerimientos](#Requerimientos-)
- [Instalación y despliegue del proyecto en localhost](#Instalación-y-despliegue-del-proyecto-en-localhost-)
- [Construido en](#Counstruido-en-%EF%B8%8F)
- [Autores](#Autores-%EF%B8%8F)

## Empezando 🚀

_Haga un fork del proyecto a su propio perfil de github, y clonelo a su propia su propia computadora en la ubicación que desee._

```
git clone <repo-link>
git add .
git commit -m <"message">
git push origin master
```

## Screenshot ⭐
![image](https://user-images.githubusercontent.com/52224826/167989427-66692809-9850-4947-be09-de7b2a2ac02c.png)


## Requerimientos 📋

_Este proyecto fue probado usando Python 3.9.5 y 3.10... No se ha testeado en otras versiones aun, pero el codigo debería ser compatible._

_Para instalar todas las dependencias necesarias para correr el proyecto se requiere adicionalmente de virtualenv. Para instalarlo, correr comando en la terminal:_

```
pip install virtualenv
```

_Nota: Asegurarse de tener la ejecucion de scripts activada en el sistema, además de tener a virtualenv agregado en las variables de entorno una vez finalizada su instalación._

## Instalación y despliegue del proyecto en localhost 🔧

_Una vez instalado virtualenv, crear entorno virtual... Posicionese en carpeta del proyecto, y ejecute el siguiente comando en la terminal:_

```
virtualenv -p python3 env
```

_Posteriormente debera activar el entorno virtual. Estando sobre la misma ruta anterior, ejecute el siguiente comando en la terminal:_

```
.\env\Scripts\activate

Si el anterior no funciona puede probar con:

env\scripts\activate

```

_Ahora, deberá instalar todas las dependencias a partir del archivo requeriments.txt. con el siguiente comando en la terminal:_

```
pip install -r .\requirements.txt
```

_Nota: Si desea desactivar entorno virtual, basta con escribir en la terminal:_

```
deactivate
```

_Una vez listo todo lo anterior, solo queda desplegar el proyecto en su localhost con el comando en la terminal:_

```
python manage.py runserver
```

_En caso de que el comando anterior falle y solicite migraciones, utilice el siguiente comando, y luego repita el paso anterior_

```
python manage.py migrate
```

_Con python manage.py runserver, se ejecutará el proyecto en localhost, la ruta de acceso será:_

```
http://127.0.0.1:8000/
```

_Finalmente, deberá rellenar el formulario, y una vez completado, hacer click en el boton para calcular la complejidad, y desplegar así el gráfico asociado_

## Counstruido en 🛠️

- [Django](http://www.djangoproject.com/)
- [Python](https://www.python.org/)
- [HTML](https://)
- [CSS](http://)
- [Javascript](https://www.javascript.com/)

## Autores ✒️

- **Marcelo De La Barrera** - [marcelodelabarrera](https://github.com/marcelodelabarrera)
- **Ariel Beroiza** - [arielberoiza](https://github.com/MemoryL3ak)
