image_path = None
audio_path = None

if image:

    image_extension = image.name.split(".")[-1].lower()

    image_path = f"uploaded_image.{image_extension}"

    with open(image_path, "wb") as f:
        f.write(image.getbuffer())


if audio:

    audio_extension = audio.name.split(".")[-1].lower()

    audio_path = f"uploaded_audio.{audio_extension}"

    with open(audio_path, "wb") as f:
        f.write(audio.getbuffer())
