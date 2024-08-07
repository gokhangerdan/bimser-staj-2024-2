import requests

# POST /load_documents/ endpoint'ine istek göndererek dokümanları yükleyin
load_response = requests.post("http://127.0.0.1:8000/load_documents/")
print("Load Documents Response Status Code:", load_response.status_code)
print("Load Documents Response Text:", load_response.text)

# Query için kullanacağınız metin
query_text = "Bu bir örnek sorgu metnidir."

# POST /query_documents/ endpoint'ine istek göndererek dokümanları sorgulayın
query = {
    "query_text": query_text,  # Metin tabanlı sorgu
    "top_k": 5
}
query_response = requests.post("http://127.0.0.1:8000/query_documents/", json=query)
print("Query Documents Response Status Code:", query_response.status_code)
print("Query Documents Response Text:", query_response.text)

# Eğer load_documents isteği başarılı ise query_documents isteğini yapın
if load_response.status_code == 200:
    query_response = requests.post("http://127.0.0.1:8000/query_documents/", json=query)
    print("Query Documents Response Status Code:", query_response.status_code)
    print("Query Documents Response Text:", query_response.text)
else:
    print("Doküman yükleme başarısız olduğu için sorgu yapmadı.")
