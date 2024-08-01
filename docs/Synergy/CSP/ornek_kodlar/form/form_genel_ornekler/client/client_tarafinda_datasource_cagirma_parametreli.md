# Client Tarafında DataSource Çağırma (Parametreli)

Client (ts) Tarafında DataSource Çağırma (Parametreli) ile ilgili  örnek kullanım aşağıdaki gibidir.

	this.fetch.post("DataSource/DataSourceAdi",{ID:373}).then(result => {
	        console.log(result);
	        }).catch((e) => {
	            console.log(e);
	        });