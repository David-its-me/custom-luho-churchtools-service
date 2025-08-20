from datetime import datetime

class CTPost():
    
    def __init__(self, post_data):
        self.post_data = post_data

    def get_url_first_image(self) -> str:
        if ('images' in self.post_data):
            post_images = self.post_data['images']
            if len(post_images) > 0:
                first_image = post_images[0]
                return first_image
        
        return None
    def get_title(self) -> str:
        if 'title' in self.post_data:
            return self.post_data['title']
        return None
    
    def get_content(self) -> str:
        if 'content' in self.post_data:
            if self.post_data['content'] is not None:
                return self.post_data['content']
        return None

    def get_group_name(self) -> str:
        if 'group' in self.post_data:
            if 'title' in self.post_data['group']:
                return self.post_data['group']['title']
        return None

    def get_author(self) -> str:
        if 'actor' in self.post_data:
            if 'title' in self.post_data['actor']:
                return self.post_data['actor']['title']
        return None

    def is_visibility_not_restricted(self) -> bool:
        if 'visibility' in self.post_data:
            if self.post_data['visibility'] is not None:
                if self.post_data['visibility'] != 'restricted':
                    return True
        return False
    
    def get_expiration_date(self) -> datetime | None:
        if 'expirationDate' in self.post_data:
            if self.post_data['expirationDate'] is not None:
                return datetime.fromisoformat(self.post_data['expirationDate'])
        return None

    def get_publication_date(self) -> datetime | None:
        if 'publicationDate' in self.post_data:
            if self.post_data['publicationDate'] is not None:
                return datetime.fromisoformat(self.post_data['publicationDate'])
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
        if 'lastEditedDate' in self.post_data:
            if self.post_data['lastEditedDate'] is not None:
                return datetime.fromisoformat(self.post_data['lastEditedDate'])
            
        if 'meta' in self.post_data:
            if 'modifiedDate' in self.post_data['meta']:
                if self.post_data['meta']['modifiedDate'] is not None:
                    return datetime.fromisoformat(self.post_data['meta']['modifiedDate'])
            
        if 'meta' in self.post_data:
            if 'createdDate' in self.post_data['meta']:
                if self.post_data['meta']['createdDate'] is not None:
                    return datetime.fromisoformat(self.post_data['meta']['createdDate'])
                
        return None
