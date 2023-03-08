from django.db import models #(username=jafar  (password=jafar12345678))

class Maincategory(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Brand(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Product(models.Model):
    id=models.AutoField(primary_key=True) 
    name=models.CharField(max_length=60)
    maincategory=models.ForeignKey(Maincategory,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    color=models.CharField(max_length=20)
    size=models.CharField(max_length=20)
    description=models.TextField()
    baseprice=models.IntegerField()
    discount=models.IntegerField(default=0,null=True,blank=True)
    finalprice=models.IntegerField()
    pic1=models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    pic2=models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    pic3=models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    pic4=models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    def __str__(self):
        return self.name

class Buyer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=30)
    phone=models.CharField(max_length=15)
    addressline1=models.CharField(max_length=150)
    addressline2=models.CharField(max_length=150)
    addressline3=models.CharField(max_length=150)
    pin=models.CharField(max_length=10)
    city=models.CharField(max_length=400)
    state=models.CharField(max_length=40)
    pic=models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    otp=models.IntegerField(default=-9823456)

    def __str__(self):
        return self.username
    
class wishlist(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(Buyer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self(self.id)+" "+self.user.username+" "+self.product.name
    

status=((0,"Order place"),(1,"Not Packed"),(2,"Packed"),(3,"Ready To Ship"),(4,"Shipped"),(5,"Out For Delivery"),(6,"Delivered"),(7,"Cancelled"))
payment=((0,"Pending"),(1,"Done"))
mode=((0,"COD"),(1,'Net Banking'))
class Checkout(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(Buyer,on_delete=models.CASCADE)
    total=models.IntegerField()
    shipping=models.IntegerField()
    final=models.IntegerField()
    rppid=models.CharField(max_length=30,default="",null=True,blank=True)
    date=models.DateTimeField(auto_now=True)
    paymentmode=models.IntegerField(choices= mode,default=0)
    paymentstatus=models.IntegerField(choices=payment,default=0)
    orderstatus=models.IntegerField(choices=status,default=0)

def __str__(self):
        return str(self.id)+" "+str(self.checkout.id)

class CheckoutProducts(models.Model):
    id = models.AutoField(primary_key=True)
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    p = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    total = models.IntegerField()
    

    def __str__(self):
        return str(self.id)+" "+str(self.checkout.id)

conatctstatus=((0,"Active"),(1,"Done"))
class Contect(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=33)
    phone=models.CharField(max_length=15)
    subject=models.CharField(max_length=50)
    message=models.TextField()
    status=models.IntegerField(choices=conatctstatus,default=0)
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return    str(self.id)+" "+self.name+" "+self.subject




















