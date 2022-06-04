# Reglas de trabajo
## para el buen desarrollo de el proyecto " **Blogtos** "


### informacion general


para **organizar** la forma en la que trabajaremos lo mejor seria definir desde ahora
el sintax que vamos a utilizar, y como escribiremos los comentarios.



### sintax del codigo y comentarios


las variables/funciones y codigo en general, se escribira en ingles.

ej:

    foo name = "Josev"
    def foo(param1,param2="default"):


ademas de que las variables seran escritas en camelCase

ej:

    nombreDeVariable = "Valor" - camelCase Bien
    NombreDeVariable = "valor" - pascalCase Mal


los comentarios en general pueden ser en español.
**lo mejor seria que solo sean utilizado para explicar y o separar secciones de codigo**

ej:
    <!--Inicio de pagina-->

        codigo...

    <!--Este codigo hace algo...-->

*o*

        #Variables globales

        #este codigo hace algo...

    

y para indentar utilizaremos tabs (4 espacios)

las strings utilizaran doble comillas

ej:

    "pepe" - Bien
    'pepe' - Mal

    *Esto es para tener mejor definido el orden*

### organizacion


para organizarnos utilizaremos trello, alli podremos ver que tenemos asignado.
ademas de que cada quien tiene una parte del trabajo

    -Backend (Fadryel)
    -FrontEnd (Paul)

    **Agregar mas luego de ser necesario**


### Archivos

**para manejar el trabajo de una mejor manera, cada quien tiene un area de trabajo asignada (*digamosle asi*)**

el codigo del **HTML** ira dentro de la carpeta templates, esto para facilitar a "Flask" el uso de la pagina
el codigo del **CSS/JS** ira dentro de la carpeta Static, esto para facilitar a "Flask" el uso del estilo

para acceder al css dentro del html desde otra carpeta en este caso **static** haremos esto

    <link rel="stylesheet" href="/static/nombreDeLaHoja.css">

*se utiliza un "/" al principio por que asi le decimos a flask en este caso que el archivo esta afuera de la carpeta templates,
luego que entre a static/styles.css*

 **El gneralStyles.css sera utilizado por **Paul** para escribir una libreria de estilo.css que puede ser utilizada genrealmente alreadedor de todas las paginas html**

 *las otras hojas de estilo seran utilizadas para estilizar una parte del html especifica.*

los archivos .py estaran fuera en el directorio local, No tocar/manipular si no es necesario.
