from datetime import datetime

class CTPost():
    
    def __init__(self, post):
        self.post = post

    def get_url_first_image(self) -> str:
        if ('images' in self.post):
            post_images = self.post['images']
            if len(post_images) > 0:
                first_image = post_images[0]
                return first_image
        
        return None
    def get_title(self) -> str:
        if 'title' in self.post:
            return self.post['title']
        return ''
    
    def get_content(self) -> str:
        if 'content' in self.post:
            if self.post['content'] is not None:
                return self.post['content']
        return ''

    def get_group_name(self) -> str:
        if 'group' in self.post:
            if 'title' in self.post['group']:
                return self.post['group']['title']
        return ''

    def get_author(self) -> str:
        if 'actor' in self.post:
            if 'title' in self.post['actor']:
                return self.post['actor']['title']
        return ''

    def is_visibility_not_restricted(self) -> bool:
        if 'visibility' in self.post:
            if self.post['visibility'] is not None:
                if self.post['visibility'] != 'restricted':
                    return True
        return False
    
    def get_expiration_date(self) -> datetime | None:
        if 'expirationDate' in self.post:
            if self.post['expirationDate'] is not None:
                return datetime.fromisoformat(self.post['expirationDate'])
        return None

    def get_publication_date(self) -> datetime | None:
        if 'publicationDate' in self.post:
            if self.post['publicationDate'] is not None:
                return datetime.fromisoformat(self.post['publicationDate'])
        return None

    def is_publicity_period_inside(self, datetime: datetime):
        publication = self.get_publication_date()
        expiration = self.get_expiration_date()
        if publication is not None:
            if publication > datetime:
                return False
        
        if expiration is not None:
            if expiration < datetime:
                return False
            
        return True
    
    def get_last_edited_date(self) -> datetime:
        if 'lastEditedDate' in self.post:
            if self.post['lastEditedDate'] is not None:
                return datetime.fromisoformat(self.post['lastEditedDate'])
            
        if 'meta' in self.post:
            if 'modifiedDate' in self.post['meta']:
                if self.post['meta']['modifiedDate'] is not None:
                    return datetime.fromisoformat(self.post['meta']['modifiedDate'])
            
        if 'meta' in self.post:
            if 'createdDate' in self.post['meta']:
                if self.post['meta']['createdDate'] is not None:
                    return datetime.fromisoformat(self.post['meta']['createdDate'])
                
        return None
