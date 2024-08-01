# Kodla Item Ekleme

Aşağıdaki kodlar kullanılarak ComboBox nesnesine item eklenebilir.

	        var tempItemList = [];
	        var newItem1 = {
	            icon: "",
	            key: "1",
	            value: "1",
	            text: {
	                defaultCulture: "tr-TR",
	                "tr-TR": "Deneme 1",
	                userCulture: "tr-TR"
	            },
	            selected: false
	        }
	        tempItemList.push(newItem1);
	        var newItem2 = {
	            icon: "",
	            key: "2",
	            value: "2",
	            text: {
	                defaultCulture: "tr-TR",
	                "tr-TR": "Deneme 2",
	                userCulture: "tr-TR"
	            },
	            selected: false
	        }
	        tempItemList.push(newItem2);
	        this.ComboBox1.items = tempItemList;