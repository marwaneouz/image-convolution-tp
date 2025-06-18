{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0b8ee7b6-04c2-40eb-aeb8-593f20f2e663",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import matplotlib.pyplot as plt\n",
    "import os\n",
    "\n",
    "# ----------------------------\n",
    "# Fonction d'affichage des images\n",
    "# ----------------------------\n",
    "def display_images(original, filtered_dict, title=\"Image Filtrée\"):\n",
    "    num_filters = len(filtered_dict)\n",
    "    fig, axes = plt.subplots(1, num_filters + 1, figsize=(5 * (num_filters + 1), 5))\n",
    "    fig.suptitle(title, fontsize=16)\n",
    "\n",
    "    # Image originale\n",
    "    if len(original.shape) == 2:\n",
    "        axes[0].imshow(original, cmap='gray')\n",
    "    else:\n",
    "        axes[0].imshow(original)\n",
    "    axes[0].set_title(\"Original\")\n",
    "    axes[0].axis('off')\n",
    "\n",
    "    # Images filtrées\n",
    "    for idx, (name, filtered) in enumerate(filtered_dict.items()):\n",
    "        if len(filtered.shape) == 2:\n",
    "            axes[idx + 1].imshow(filtered, cmap='gray')\n",
    "        else:\n",
    "            axes[idx + 1].imshow(filtered)\n",
    "        axes[idx + 1].set_title(name)\n",
    "        axes[idx + 1].axis('off')\n",
    "\n",
    "    plt.tight_layout()\n",
    "    plt.show()\n",
    "\n",
    "# ----------------------------\n",
    "# Fonction de sauvegarde des images\n",
    "# ----------------------------\n",
    "def save_images(save_dir, original_name, filtered_dict):\n",
    "    os.makedirs(save_dir, exist_ok=True)\n",
    "    base_name = os.path.splitext(os.path.basename(original_name))[0]\n",
    "\n",
    "    for name, img in filtered_dict.items():\n",
    "        filename = f\"{base_name}_{name}.jpg\"\n",
    "        path = os.path.join(save_dir, filename)\n",
    "        if len(img.shape) == 3:\n",
    "            img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)\n",
    "        else:\n",
    "            img_bgr = img\n",
    "        cv2.imwrite(path, img_bgr)\n",
    "        print(f\"Saved: {path}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7ec5185b-e66b-4913-96d8-f22f4064e527",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'src'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[4], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msrc\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mutils\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m image_load\n\u001b[0;32m      3\u001b[0m img_original \u001b[38;5;241m=\u001b[39m image_load(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mimages/original/image.jpg\u001b[39m\u001b[38;5;124m\"\u001b[39m, channel\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m3\u001b[39m)\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'src'"
     ]
    }
   ],
   "source": [
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8c88b1b-cef7-45fd-a1c6-b5a60400c1c5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
