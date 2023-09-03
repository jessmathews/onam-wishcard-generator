from PIL import Image, ImageDraw, ImageFont


def generate_wish_card_image(image,sender,receiver):
    if (image == "onam_1"):
        image=Image.open('static/cards/'+image+'.png')
        font_size = 36
        font = ImageFont.truetype('fonts/WindSong-Medium.ttf',font_size)
        font_color =(82,44,20)
        draw = ImageDraw.Draw(image)
        position = (120,360) 
        draw.text(position,"Regards, "+sender,font=font,fill=font_color)
        image.save(f"generated_cards/output_image_{sender.lower()}.png")
        return True

    elif (image == "onam_2"):
        image=Image.open('static/cards/'+image+'.png')
        font_size = 40
        font = ImageFont.truetype('fonts/WindSong-Medium.ttf',font_size)
        font_color =(164,69,3)
        draw = ImageDraw.Draw(image)
        position = (120,310) 
        draw.text(position,"Regards, "+sender,font=font,fill=font_color)
        image.save(f"generated_cards/output_image_{sender.lower()}.png")
        return True

    elif (image == "onam_3"):
        image=Image.open('static/cards/'+image+'.png')
        font_size = 40
        font = ImageFont.truetype('fonts/WindSong-Medium.ttf',font_size)
        font_color =(251,186,77)
        draw = ImageDraw.Draw(image)
        position = (120,390) 
        draw.text(position,"Regards, "+sender,font=font,fill=font_color)
        image.save(f"generated_cards/output_image_{sender.lower()}.png")
        return True

    elif (image == "onam_4"):
        image=Image.open('static/cards/'+image+'.png')
        font_size = 40
        font = ImageFont.truetype('fonts/WindSong-Medium.ttf',font_size)
        font_color =(255,255,255)
        draw = ImageDraw.Draw(image)
        position = (120,440) 
        draw.text(position,"Regards, "+sender,font=font,fill=font_color)
        image.save(f"generated_cards/output_image_{sender.lower()}.png")
        return True

    
    elif (image == "onam_5"):
        image=Image.open('static/cards/'+image+'.png')
        font_size = 40
        font = ImageFont.truetype('fonts/WindSong-Medium.ttf',font_size)
        font_color =(252,128,1)
        draw = ImageDraw.Draw(image)
        position = (120,340) 
        draw.text(position,"Regards, "+sender,font=font,fill=font_color)
        image.save(f"generated_cards/output_image_{sender.lower()}.png")
        return True
    else:
        return False