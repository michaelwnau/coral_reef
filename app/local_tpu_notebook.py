{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNn3gUfyH7SUdzFbDTM7JKF",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/michaelwnau/coral_reef/blob/main/local_tpu_notebook.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Notebook + TPU. Concept: a Jupyter Notebook that utilizes a local Google Coral TPU device. No cloud, no VM, lowest cost after initial investment, able to run in a edge TPU scenario."
      ],
      "metadata": {
        "id": "fvr4yBVRRS8l"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RnHLlqFPPj44",
        "outputId": "e7ba8ab5-e924-4f4a-f70a-b2136ae982fe"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: jupyterlab in /usr/local/lib/python3.9/dist-packages (3.6.3)\n",
            "Requirement already satisfied: nbclassic in /usr/local/lib/python3.9/dist-packages (from jupyterlab) (0.5.5)\n",
            "Requirement already satisfied: jupyter-server<3,>=1.16.0 in /usr/local/lib/python3.9/dist-packages (from jupyterlab) (1.23.6)\n",
            "Requirement already satisfied: jupyterlab-server~=2.19 in /usr/local/lib/python3.9/dist-packages (from jupyterlab) (2.22.0)\n",
            "Requirement already satisfied: jinja2>=2.1 in /usr/local/lib/python3.9/dist-packages (from jupyterlab) (3.1.2)\n",
            "Requirement already satisfied: jupyter-ydoc~=0.2.3 in /usr/local/lib/python3.9/dist-packages (from jupyterlab) (0.2.3)\n",
            "Requirement already satisfied: jupyter-server-ydoc~=0.8.0 in /usr/local/lib/python3.9/dist-packages (from jupyterlab) (0.8.0)\n",
            "Requirement already satisfied: notebook<7 in /usr/local/lib/python3.9/dist-packages (from jupyterlab) (6.4.8)\n",
            "Requirement already satisfied: tornado>=6.1.0 in /usr/local/lib/python3.9/dist-packages (from jupyterlab) (6.2)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.9/dist-packages (from jupyterlab) (23.0)\n",
            "Requirement already satisfied: tomli in /usr/local/lib/python3.9/dist-packages (from jupyterlab) (2.0.1)\n",
            "Requirement already satisfied: ipython in /usr/local/lib/python3.9/dist-packages (from jupyterlab) (7.34.0)\n",
            "Requirement already satisfied: jupyter-core in /usr/local/lib/python3.9/dist-packages (from jupyterlab) (5.3.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.9/dist-packages (from jinja2>=2.1->jupyterlab) (2.1.2)\n",
            "Requirement already satisfied: nbformat>=5.2.0 in /usr/local/lib/python3.9/dist-packages (from jupyter-server<3,>=1.16.0->jupyterlab) (5.8.0)\n",
            "Requirement already satisfied: websocket-client in /usr/local/lib/python3.9/dist-packages (from jupyter-server<3,>=1.16.0->jupyterlab) (1.5.1)\n",
            "Requirement already satisfied: traitlets>=5.1 in /usr/local/lib/python3.9/dist-packages (from jupyter-server<3,>=1.16.0->jupyterlab) (5.7.1)\n",
            "Requirement already satisfied: prometheus-client in /usr/local/lib/python3.9/dist-packages (from jupyter-server<3,>=1.16.0->jupyterlab) (0.16.0)\n",
            "Requirement already satisfied: jupyter-client>=6.1.12 in /usr/local/lib/python3.9/dist-packages (from jupyter-server<3,>=1.16.0->jupyterlab) (6.1.12)\n",
            "Requirement already satisfied: terminado>=0.8.3 in /usr/local/lib/python3.9/dist-packages (from jupyter-server<3,>=1.16.0->jupyterlab) (0.17.1)\n",
            "Requirement already satisfied: anyio<4,>=3.1.0 in /usr/local/lib/python3.9/dist-packages (from jupyter-server<3,>=1.16.0->jupyterlab) (3.6.2)\n",
            "Requirement already satisfied: pyzmq>=17 in /usr/local/lib/python3.9/dist-packages (from jupyter-server<3,>=1.16.0->jupyterlab) (23.2.1)\n",
            "Requirement already satisfied: Send2Trash in /usr/local/lib/python3.9/dist-packages (from jupyter-server<3,>=1.16.0->jupyterlab) (1.8.0)\n",
            "Requirement already satisfied: nbconvert>=6.4.4 in /usr/local/lib/python3.9/dist-packages (from jupyter-server<3,>=1.16.0->jupyterlab) (6.5.4)\n",
            "Requirement already satisfied: argon2-cffi in /usr/local/lib/python3.9/dist-packages (from jupyter-server<3,>=1.16.0->jupyterlab) (21.3.0)\n",
            "Requirement already satisfied: platformdirs>=2.5 in /usr/local/lib/python3.9/dist-packages (from jupyter-core->jupyterlab) (3.2.0)\n",
            "Requirement already satisfied: jupyter-server-fileid<1,>=0.6.0 in /usr/local/lib/python3.9/dist-packages (from jupyter-server-ydoc~=0.8.0->jupyterlab) (0.8.0)\n",
            "Requirement already satisfied: ypy-websocket<0.9.0,>=0.8.2 in /usr/local/lib/python3.9/dist-packages (from jupyter-server-ydoc~=0.8.0->jupyterlab) (0.8.2)\n",
            "Requirement already satisfied: y-py<0.6.0,>=0.5.3 in /usr/local/lib/python3.9/dist-packages (from jupyter-ydoc~=0.2.3->jupyterlab) (0.5.9)\n",
            "Requirement already satisfied: importlib-metadata>=3.6 in /usr/local/lib/python3.9/dist-packages (from jupyter-ydoc~=0.2.3->jupyterlab) (6.1.0)\n",
            "Requirement already satisfied: jsonschema>=4.17.3 in /usr/local/lib/python3.9/dist-packages (from jupyterlab-server~=2.19->jupyterlab) (4.17.3)\n",
            "Requirement already satisfied: json5>=0.9.0 in /usr/local/lib/python3.9/dist-packages (from jupyterlab-server~=2.19->jupyterlab) (0.9.11)\n",
            "Requirement already satisfied: babel>=2.10 in /usr/local/lib/python3.9/dist-packages (from jupyterlab-server~=2.19->jupyterlab) (2.12.1)\n",
            "Requirement already satisfied: requests>=2.28 in /usr/local/lib/python3.9/dist-packages (from jupyterlab-server~=2.19->jupyterlab) (2.28.2)\n",
            "Requirement already satisfied: ipykernel in /usr/local/lib/python3.9/dist-packages (from notebook<7->jupyterlab) (5.5.6)\n",
            "Requirement already satisfied: nest-asyncio>=1.5 in /usr/local/lib/python3.9/dist-packages (from notebook<7->jupyterlab) (1.5.6)\n",
            "Requirement already satisfied: ipython-genutils in /usr/local/lib/python3.9/dist-packages (from notebook<7->jupyterlab) (0.2.0)\n",
            "Requirement already satisfied: jedi>=0.16 in /usr/local/lib/python3.9/dist-packages (from ipython->jupyterlab) (0.18.2)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.9/dist-packages (from ipython->jupyterlab) (4.4.2)\n",
            "Requirement already satisfied: pexpect>4.3 in /usr/local/lib/python3.9/dist-packages (from ipython->jupyterlab) (4.8.0)\n",
            "Requirement already satisfied: matplotlib-inline in /usr/local/lib/python3.9/dist-packages (from ipython->jupyterlab) (0.1.6)\n",
            "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /usr/local/lib/python3.9/dist-packages (from ipython->jupyterlab) (3.0.38)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.9/dist-packages (from ipython->jupyterlab) (0.7.5)\n",
            "Requirement already satisfied: setuptools>=18.5 in /usr/local/lib/python3.9/dist-packages (from ipython->jupyterlab) (67.6.1)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.9/dist-packages (from ipython->jupyterlab) (2.14.0)\n",
            "Requirement already satisfied: backcall in /usr/local/lib/python3.9/dist-packages (from ipython->jupyterlab) (0.2.0)\n",
            "Requirement already satisfied: notebook-shim>=0.1.0 in /usr/local/lib/python3.9/dist-packages (from nbclassic->jupyterlab) (0.2.2)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.9/dist-packages (from anyio<4,>=3.1.0->jupyter-server<3,>=1.16.0->jupyterlab) (1.3.0)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.9/dist-packages (from anyio<4,>=3.1.0->jupyter-server<3,>=1.16.0->jupyterlab) (3.4)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.9/dist-packages (from importlib-metadata>=3.6->jupyter-ydoc~=0.2.3->jupyterlab) (3.15.0)\n",
            "Requirement already satisfied: parso<0.9.0,>=0.8.0 in /usr/local/lib/python3.9/dist-packages (from jedi>=0.16->ipython->jupyterlab) (0.8.3)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.9/dist-packages (from jsonschema>=4.17.3->jupyterlab-server~=2.19->jupyterlab) (0.19.3)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.9/dist-packages (from jsonschema>=4.17.3->jupyterlab-server~=2.19->jupyterlab) (22.2.0)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.9/dist-packages (from jupyter-client>=6.1.12->jupyter-server<3,>=1.16.0->jupyterlab) (2.8.2)\n",
            "Requirement already satisfied: jupyter-events>=0.5.0 in /usr/local/lib/python3.9/dist-packages (from jupyter-server-fileid<1,>=0.6.0->jupyter-server-ydoc~=0.8.0->jupyterlab) (0.6.3)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.9/dist-packages (from nbconvert>=6.4.4->jupyter-server<3,>=1.16.0->jupyterlab) (0.7.1)\n",
            "Requirement already satisfied: entrypoints>=0.2.2 in /usr/local/lib/python3.9/dist-packages (from nbconvert>=6.4.4->jupyter-server<3,>=1.16.0->jupyterlab) (0.4)\n",
            "Requirement already satisfied: lxml in /usr/local/lib/python3.9/dist-packages (from nbconvert>=6.4.4->jupyter-server<3,>=1.16.0->jupyterlab) (4.9.2)\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.9/dist-packages (from nbconvert>=6.4.4->jupyter-server<3,>=1.16.0->jupyterlab) (4.11.2)\n",
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.9/dist-packages (from nbconvert>=6.4.4->jupyter-server<3,>=1.16.0->jupyterlab) (1.5.0)\n",
            "Requirement already satisfied: nbclient>=0.5.0 in /usr/local/lib/python3.9/dist-packages (from nbconvert>=6.4.4->jupyter-server<3,>=1.16.0->jupyterlab) (0.7.3)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.9/dist-packages (from nbconvert>=6.4.4->jupyter-server<3,>=1.16.0->jupyterlab) (6.0.0)\n",
            "Requirement already satisfied: jupyterlab-pygments in /usr/local/lib/python3.9/dist-packages (from nbconvert>=6.4.4->jupyter-server<3,>=1.16.0->jupyterlab) (0.2.2)\n",
            "Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.9/dist-packages (from nbconvert>=6.4.4->jupyter-server<3,>=1.16.0->jupyterlab) (0.8.4)\n",
            "Requirement already satisfied: tinycss2 in /usr/local/lib/python3.9/dist-packages (from nbconvert>=6.4.4->jupyter-server<3,>=1.16.0->jupyterlab) (1.2.1)\n",
            "Requirement already satisfied: fastjsonschema in /usr/local/lib/python3.9/dist-packages (from nbformat>=5.2.0->jupyter-server<3,>=1.16.0->jupyterlab) (2.16.3)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.9/dist-packages (from pexpect>4.3->ipython->jupyterlab) (0.7.0)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.9/dist-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython->jupyterlab) (0.2.6)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.9/dist-packages (from requests>=2.28->jupyterlab-server~=2.19->jupyterlab) (1.26.15)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.9/dist-packages (from requests>=2.28->jupyterlab-server~=2.19->jupyterlab) (2.0.12)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.9/dist-packages (from requests>=2.28->jupyterlab-server~=2.19->jupyterlab) (2022.12.7)\n",
            "Requirement already satisfied: aiosqlite<1,>=0.17.0 in /usr/local/lib/python3.9/dist-packages (from ypy-websocket<0.9.0,>=0.8.2->jupyter-server-ydoc~=0.8.0->jupyterlab) (0.18.0)\n",
            "Requirement already satisfied: aiofiles<23,>=22.1.0 in /usr/local/lib/python3.9/dist-packages (from ypy-websocket<0.9.0,>=0.8.2->jupyter-server-ydoc~=0.8.0->jupyterlab) (22.1.0)\n",
            "Requirement already satisfied: argon2-cffi-bindings in /usr/local/lib/python3.9/dist-packages (from argon2-cffi->jupyter-server<3,>=1.16.0->jupyterlab) (21.2.0)\n",
            "Requirement already satisfied: python-json-logger>=2.0.4 in /usr/local/lib/python3.9/dist-packages (from jupyter-events>=0.5.0->jupyter-server-fileid<1,>=0.6.0->jupyter-server-ydoc~=0.8.0->jupyterlab) (2.0.7)\n",
            "Requirement already satisfied: rfc3339-validator in /usr/local/lib/python3.9/dist-packages (from jupyter-events>=0.5.0->jupyter-server-fileid<1,>=0.6.0->jupyter-server-ydoc~=0.8.0->jupyterlab) (0.1.4)\n",
            "Requirement already satisfied: pyyaml>=5.3 in /usr/local/lib/python3.9/dist-packages (from jupyter-events>=0.5.0->jupyter-server-fileid<1,>=0.6.0->jupyter-server-ydoc~=0.8.0->jupyterlab) (6.0)\n",
            "Requirement already satisfied: rfc3986-validator>=0.1.1 in /usr/local/lib/python3.9/dist-packages (from jupyter-events>=0.5.0->jupyter-server-fileid<1,>=0.6.0->jupyter-server-ydoc~=0.8.0->jupyterlab) (0.1.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.9/dist-packages (from python-dateutil>=2.1->jupyter-client>=6.1.12->jupyter-server<3,>=1.16.0->jupyterlab) (1.16.0)\n",
            "Requirement already satisfied: cffi>=1.0.1 in /usr/local/lib/python3.9/dist-packages (from argon2-cffi-bindings->argon2-cffi->jupyter-server<3,>=1.16.0->jupyterlab) (1.15.1)\n",
            "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.9/dist-packages (from beautifulsoup4->nbconvert>=6.4.4->jupyter-server<3,>=1.16.0->jupyterlab) (2.4)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.9/dist-packages (from bleach->nbconvert>=6.4.4->jupyter-server<3,>=1.16.0->jupyterlab) (0.5.1)\n",
            "Requirement already satisfied: pycparser in /usr/local/lib/python3.9/dist-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi->jupyter-server<3,>=1.16.0->jupyterlab) (2.21)\n",
            "Requirement already satisfied: webcolors>=1.11 in /usr/local/lib/python3.9/dist-packages (from jsonschema>=4.17.3->jupyterlab-server~=2.19->jupyterlab) (1.13)\n",
            "Requirement already satisfied: fqdn in /usr/local/lib/python3.9/dist-packages (from jsonschema>=4.17.3->jupyterlab-server~=2.19->jupyterlab) (1.5.1)\n",
            "Requirement already satisfied: uri-template in /usr/local/lib/python3.9/dist-packages (from jsonschema>=4.17.3->jupyterlab-server~=2.19->jupyterlab) (1.2.0)\n",
            "Requirement already satisfied: isoduration in /usr/local/lib/python3.9/dist-packages (from jsonschema>=4.17.3->jupyterlab-server~=2.19->jupyterlab) (20.11.0)\n",
            "Requirement already satisfied: jsonpointer>1.13 in /usr/local/lib/python3.9/dist-packages (from jsonschema>=4.17.3->jupyterlab-server~=2.19->jupyterlab) (2.3)\n",
            "Requirement already satisfied: arrow>=0.15.0 in /usr/local/lib/python3.9/dist-packages (from isoduration->jsonschema>=4.17.3->jupyterlab-server~=2.19->jupyterlab) (1.2.3)\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: pycoral in /usr/local/lib/python3.9/dist-packages (0.1.0)\n",
            "Requirement already satisfied: requests>=2.23.1 in /usr/local/lib/python3.9/dist-packages (from pycoral) (2.28.2)\n",
            "Requirement already satisfied: beautifulsoup4>=4.9.0 in /usr/local/lib/python3.9/dist-packages (from pycoral) (4.11.2)\n",
            "Requirement already satisfied: geojson>=2.4.1 in /usr/local/lib/python3.9/dist-packages (from pycoral) (3.0.1)\n",
            "Requirement already satisfied: progressbar2>=3.53.1 in /usr/local/lib/python3.9/dist-packages (from pycoral) (4.2.0)\n",
            "Requirement already satisfied: area>=1.1.1 in /usr/local/lib/python3.9/dist-packages (from pycoral) (1.1.1)\n",
            "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.9/dist-packages (from beautifulsoup4>=4.9.0->pycoral) (2.4)\n",
            "Requirement already satisfied: python-utils>=3.0.0 in /usr/local/lib/python3.9/dist-packages (from progressbar2>=3.53.1->pycoral) (3.5.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.9/dist-packages (from requests>=2.23.1->pycoral) (2.0.12)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.9/dist-packages (from requests>=2.23.1->pycoral) (2022.12.7)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.9/dist-packages (from requests>=2.23.1->pycoral) (1.26.15)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.9/dist-packages (from requests>=2.23.1->pycoral) (3.4)\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: nbformat in /usr/local/lib/python3.9/dist-packages (5.8.0)\n",
            "Requirement already satisfied: nbconvert in /usr/local/lib/python3.9/dist-packages (6.5.4)\n",
            "Collecting nbconvert\n",
            "  Downloading nbconvert-7.3.0-py3-none-any.whl (284 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m284.0/284.0 KB\u001b[0m \u001b[31m6.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: jupyter-core in /usr/local/lib/python3.9/dist-packages (from nbformat) (5.3.0)\n",
            "Requirement already satisfied: fastjsonschema in /usr/local/lib/python3.9/dist-packages (from nbformat) (2.16.3)\n",
            "Requirement already satisfied: jsonschema>=2.6 in /usr/local/lib/python3.9/dist-packages (from nbformat) (4.17.3)\n",
            "Requirement already satisfied: traitlets>=5.1 in /usr/local/lib/python3.9/dist-packages (from nbformat) (5.7.1)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.9/dist-packages (from nbconvert) (6.0.0)\n",
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.9/dist-packages (from nbconvert) (1.5.0)\n",
            "Requirement already satisfied: nbclient>=0.5.0 in /usr/local/lib/python3.9/dist-packages (from nbconvert) (0.7.3)\n",
            "Requirement already satisfied: jinja2>=3.0 in /usr/local/lib/python3.9/dist-packages (from nbconvert) (3.1.2)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.9/dist-packages (from nbconvert) (23.0)\n",
            "Requirement already satisfied: jupyterlab-pygments in /usr/local/lib/python3.9/dist-packages (from nbconvert) (0.2.2)\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.9/dist-packages (from nbconvert) (4.11.2)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.9/dist-packages (from nbconvert) (0.7.1)\n",
            "Collecting mistune<3,>=2.0.3\n",
            "  Downloading mistune-2.0.5-py2.py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: pygments>=2.4.1 in /usr/local/lib/python3.9/dist-packages (from nbconvert) (2.14.0)\n",
            "Requirement already satisfied: markupsafe>=2.0 in /usr/local/lib/python3.9/dist-packages (from nbconvert) (2.1.2)\n",
            "Requirement already satisfied: tinycss2 in /usr/local/lib/python3.9/dist-packages (from nbconvert) (1.2.1)\n",
            "Requirement already satisfied: importlib-metadata>=3.6 in /usr/local/lib/python3.9/dist-packages (from nbconvert) (6.1.0)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.9/dist-packages (from importlib-metadata>=3.6->nbconvert) (3.15.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.9/dist-packages (from jsonschema>=2.6->nbformat) (0.19.3)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.9/dist-packages (from jsonschema>=2.6->nbformat) (22.2.0)\n",
            "Requirement already satisfied: platformdirs>=2.5 in /usr/local/lib/python3.9/dist-packages (from jupyter-core->nbformat) (3.2.0)\n",
            "Requirement already satisfied: jupyter-client>=6.1.12 in /usr/local/lib/python3.9/dist-packages (from nbclient>=0.5.0->nbconvert) (6.1.12)\n",
            "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.9/dist-packages (from beautifulsoup4->nbconvert) (2.4)\n",
            "Requirement already satisfied: six>=1.9.0 in /usr/local/lib/python3.9/dist-packages (from bleach->nbconvert) (1.16.0)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.9/dist-packages (from bleach->nbconvert) (0.5.1)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.9/dist-packages (from jupyter-client>=6.1.12->nbclient>=0.5.0->nbconvert) (2.8.2)\n",
            "Requirement already satisfied: pyzmq>=13 in /usr/local/lib/python3.9/dist-packages (from jupyter-client>=6.1.12->nbclient>=0.5.0->nbconvert) (23.2.1)\n",
            "Requirement already satisfied: tornado>=4.1 in /usr/local/lib/python3.9/dist-packages (from jupyter-client>=6.1.12->nbclient>=0.5.0->nbconvert) (6.2)\n",
            "Installing collected packages: mistune, nbconvert\n",
            "  Attempting uninstall: mistune\n",
            "    Found existing installation: mistune 0.8.4\n",
            "    Uninstalling mistune-0.8.4:\n",
            "      Successfully uninstalled mistune-0.8.4\n",
            "  Attempting uninstall: nbconvert\n",
            "    Found existing installation: nbconvert 6.5.4\n",
            "    Uninstalling nbconvert-6.5.4:\n",
            "      Successfully uninstalled nbconvert-6.5.4\n",
            "Successfully installed mistune-2.0.5 nbconvert-7.3.0\n"
          ]
        }
      ],
      "source": [
        "!pip install jupyterlab\n",
        "!pip install pycoral\n",
        "!pip install --upgrade nbformat nbconvert"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Dependencies to run this notebook can be downloaded here: https://coral.ai/docs/notes/build-coral/#required-components"
      ],
      "metadata": {
        "id": "vYdleLbLQtNI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from jupyter_core.command import main as jupyter\n",
        "import os\n",
        "from pycoral.adapters import classify, common\n",
        "from pycoral.utils.edgetpu import make_interpreter"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 357
        },
        "id": "TDY6J1PdPoDk",
        "outputId": "dcb9bf45-8eae-46e7-a1a0-4073aeaeddc6"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-8-0e3a61f5aa70>\u001b[0m in \u001b[0;36m<cell line: 3>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mjupyter_core\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mmain\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mjupyter\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mos\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mpycoral\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0madapters\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mclassify\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcommon\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mpycoral\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mutils\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0medgetpu\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mmake_interpreter\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'pycoral.adapters'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Set the path to the TPU device\n",
        "TPU_DEVICE_PATH = '/dev/apex_0'"
      ],
      "metadata": {
        "id": "Gmu507ZmPriV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Connect to the TPU\n",
        "interpreter = make_interpreter(TPU_DEVICE_PATH)\n",
        "interpreter.allocate_tensors()"
      ],
      "metadata": {
        "id": "zA5mBkKvPxjB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Set the Jupyter Notebook configuration options\n",
        "config_file = \"/path/to/jupyter_notebook_config.py\"\n",
        "options = f\"--NotebookApp.allow_origin='*' --NotebookApp.ip='0.0.0.0' \\\n",
        "    --NotebookApp.port=8888 --NotebookApp.notebook_dir='/content' \\\n",
        "    --NotebookApp.token='' --NotebookApp.password='' \\\n",
        "    --Session.key=''\""
      ],
      "metadata": {
        "id": "JXAGuUFkP6aH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Start the Jupyter Notebook server with TPU support\n",
        "jupyter(['notebook', '--config', config_file, options])"
      ],
      "metadata": {
        "id": "iTDpoA0cQAtn"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}