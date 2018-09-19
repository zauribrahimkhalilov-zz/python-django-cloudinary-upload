from django.shortcuts import render, redirect
from django.views import View

from cloudinaryupload.forms import UploadForm
from cloudinaryupload.models import ImageUpload

import cloudinary


class IndexView(View):
    template_name = 'pages/index.html'

    def get(self, request):
        form = UploadForm()
        image_list = ImageUpload.objects.all()
        context = { "form": form, "image_list": image_list }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UploadForm(request.POST, request.FILES)

        if request.method == 'POST':
            image_upload = ImageUpload()
            image_upload.image = request.FILES['image']
            form.save()

            try:
                cloudinary.uploader.upload(request.FILES['image'])
                return redirect("/")
            except:
                return redirect("/")

