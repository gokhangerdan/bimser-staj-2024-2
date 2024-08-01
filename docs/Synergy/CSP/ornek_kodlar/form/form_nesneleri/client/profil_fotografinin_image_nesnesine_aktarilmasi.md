# Profil Fotoğrafının Image Nesnesine Aktarılması

```

  async Button2_OnClick(args: Controls.EventArgs.IClickEventArgs) {
        const userDetail: any = await this.fetch.get("https://cspdestek.bimser.net/api/web/hr/Users/GetUserDetail", {});
        let imgValue = userDetail;

        let imgUrl = `https://cspdestek.bimser.net/api/web${imgValue.data.info.profileImage}`;

        this.Image1.fileName = imgUrl;
    }
```

