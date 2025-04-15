clone this.
Update pdf files in assets
to see the files in assets call this URL http://127.0.0.1:8000/api/list-pdfs/

after getting this files you can do post call.
curl --location 'http://127.0.0.1:8000/api/summarize-pdf/' \
--header 'Content-Type: text/plain' \
--data '{
  "filename": "any_pdf_name_here.pdf"
}'


OR


open this in chrome http://localhost:8000/api/ 




copy
pdfreader and assets(it has sample pdfs) folder completely 
copy .env, Dockerfile, requirements.txt,.gitignore and assets
 add below url in your main project urls.
  path('api/', include('pdfreader.urls')),


ask interviwer to give command "docker compose up --build"