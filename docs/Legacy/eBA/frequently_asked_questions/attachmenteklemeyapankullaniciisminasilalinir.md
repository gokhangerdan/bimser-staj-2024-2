# Attachment Ekleme Yapan Kullanıcı İsmi Nasıl Alınır

```public void Attachment1_OnAfterAttach(object sender, eBAAttachmentFileEventArgs e)
{
          string attachedUser = string.Empty;
            eBAAttachments eBAAttachments = new eBAAttachments();
            foreach (var item in Attachment1.Categories)
            {
                foreach (var item2 in item.Files)
                {
                    attachedUser+=item2.AttachedUser;
                }
            }
 
            Text1.Text=attachedUser;
}```

