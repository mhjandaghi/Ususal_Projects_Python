from abc import ABC, abstractmethod

# Before SRP
class BlogPost:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def format_markdown(self) -> str:
        return f"# {self.title}\n\n{self.content}"

    def publish_to_wordpress(self):
        formatted = self.format_markdown()
        print(f"Connecting to WordPress API...")
        print(f"Uploading post: {formatted}")
# مشکل اینجا این تک وظیفه ای نیست کلاس ما و داریم از دامنه وظایف خارج میشمیم و بهش میگیم که برامون عملیات انتشار انجام بده

 
# ------------------------------
# After SRP
class BlogPost:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def format_markdown(self) -> str:
        return f"# {self.title}\n\n{self.content}"

class Publisher:
    def publish(self,provider, post):
        if provider == "wordpress":
            formatted = post.format_markdown()
            print(f"Connecting to {provider} API...")
            print(f"Uploading post: {formatted}")
        elif provider == "Medium":
            formatted = post.format_markdown()
            print(f"Connecting to {provider} API...")
            print(f"Uploading post: {formatted}")
# مشکل اینجا اینه که برای گسترش یا تغییر بقیه اعضا درگیر میشن که مناسب نیست      
            
# ------------------------------
# After OCP
class BlogPost:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def format_markdown(self):
        return f"# {self.title}\n\n{self.content}"

class Publisher(ABC):
    @abstractmethod
    def publish(self):
        pass

class WordPressPublisher(Publisher):
    def publish(self, post):
        print(f"Uploading to WordPress")

class MediumPublisher(Publisher):
    def publish(self, post):
        print(f"Uploading to Medium")

class DraftPublisher(Publisher):
    def publish(self, post,save_path):
        print(f"Saving as draft to: {save_path}")

# مشکل اینجا اینه که ما طبق سالید نباید کلاس مادر با توجه به وراثت به مشکل بخوره ولی درفت این رو نقض کرد

# ------------------------------
# After LSP
class BlogPost:
    def __init__(self,title,content):
        self.title  = title 
        self.content = content
        
    def format_markdown(self):
        return f"# {self.title} \n\n{self.content}"

class Publisher(ABC):
    @abstractmethod
    def publish(self):
        pass
    
    @abstractmethod
    def schedule(self):
        pass
    @abstractmethod
    def get_analysis(self):
        pass

class DraftPublisher(Publisher):
    def __init__(self,save_path):
        self.save_path = save_path
        
    def publish(self,post):
        data = post.format_markdown()
        print(f"-> starting to connect draft and saving the post in {self.save_path}")
        print("-> post has been published")

class MediumPublisher(Publisher):
    def publish(self,post):
        data = post.format_markdown()
        print("-> starting to connect medium and publishing the post")
        print("-> post has been published")
        
# مشکل اینجاست که همه منتشر کننده ها نیاز به همه رفتار ها نداره پس این کلاس هارو جدا میکنیم تا هرکدوم مدیریت شن  
      
# ------------------------------
# After ISP

class BlogPost:
    def __init__(self,title,content):
        self.title  = title 
        self.content = content
        
    def format_markdown(self):
        return f"# {self.title} \n\n{self.content}"

class Publishable(ABC):
    @abstractmethod
    def publish(self):
        pass
    
class Schedulable(ABC):
    @abstractmethod
    def schedule(self):
        pass

class Analyzable(ABC):
    @abstractmethod
    def get_analysis(self):
        pass

class WordpressPublisher(Publishable,Schedulable):
    def publish(self,post):
        data = post.format_markdown()
        print("-> starting to connect wordpress and publishing the post")
        print("-> post has been published")
        
    def schedule(self,publish_date,post):
        data = post.format_markdown()
        print("-> starting to connect wordpress and schedule the post")
        print("-> post has been scheduled")
        

class MediumPublisher(Publishable):
    def publish(self,post):
        data = post.format_markdown()
        print("-> starting to connect medium and publishing the post")
        print("-> post has been published")
    
class DraftPublisher(Publishable):
    def __init__(self,save_path):
        self.save_path = save_path
        
    def publish(self,post):
        data = post.format_markdown()
        print(f"-> starting to connect draft and saving the post in {self.save_path}")
        print("-> post has been published")

post = BlogPost(title="python programming",content="programming python is easy")

class CMSWorker: 
    
    def __init__(self,publisher):
        self.publisher = WordpressPublisher()
        
    def run_publish_pipeline(self,post):
        # process 
        self.publisher.publish(post)


# ------------------------------
# After DIP
class BlogPost:
    def __init__(self,title,content):
        self.title  = title 
        self.content = content
        
    def format_markdown(self):
        return f"# {self.title} \n\n{self.content}"

class Publishable(ABC):
    @abstractmethod
    def publish(self):
        pass
    
class Schedulable(ABC):
    @abstractmethod
    def schedule(self):
        pass

class Analyzable(ABC):
    @abstractmethod
    def get_analysis(self):
        pass

class WordpressPublisher(Publishable,Schedulable):
    def publish(self,post):
        data = post.format_markdown()
        print("-> starting to connect wordpress and publishing the post")
        print("-> post has been published")
        
    def schedule(self,publish_date,post):
        data = post.format_markdown()
        print("-> starting to connect wordpress and schedule the post")
        print("-> post has been scheduled")
        

class MediumPublisher(Publishable):
    def publish(self,post):
        data = post.format_markdown()
        print("-> starting to connect medium and publishing the post")
        print("-> post has been published")
    
class DraftPublisher(Publishable):
    def __init__(self,save_path):
        self.save_path = save_path
        
    def publish(self,post):
        data = post.format_markdown()
        print(f"-> starting to connect draft and saving the post in {self.save_path}")
        print("-> post has been published")

post = BlogPost(title="python programming",content="programming python is easy")

class CMSWorker: # DIP
    
    def __init__(self,publisher):
        self.publisher = publisher
        
    def run_publish_pipeline(self,post):
        # process 
        self.publisher.publish(post)