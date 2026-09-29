#Algumas definições importantes para o estudo de módulos:
# 1º Módulo: unidade de código carregável/importável pelo Python; frequentemente corresponde a um arquivo .py, mesmo que ele não contenha variáveis, classes ou funções próprias.
# 2º Pacotes: estruturas que agrupam módulos relacionados. Pacotes regulares usam __init__.py; também existem namespace packages, que podem existir sem esse arquivo.
# 3º Bibliotecas: conjuntos de módulos/pacotes relacionados que fornecem funcionalidades; podem fazer parte da biblioteca padrão ou ser de terceiros.

#-------//-----------------//----------------------//--------------------

# ==============================================================================
# INVENTÁRIO QUASE COMPLETO DA BIBLIOTECA PADRÃO (SISTEMATIZADO)
# ==============================================================================

# region | PROCESSAMENTO DE TEXTO
import string     # Operações comuns com strings (letras, dígitos, pontuação).
import re         # Expressões regulares (busca de padrões complexos).
import difflib    # Auxílio para calcular e trabalhar com diferenças entre textos.
import textwrap   # Formatação e quebra de parágrafos de texto.
import unicodedata # Banco de dados de caracteres Unicode.
import stringprep # Preparação de strings para protocolos de rede.
import readline   # Interface para o GNU Readline (histórico de comandos).
import rlcompleter # Autocompletar para o readline.
# endregion

# region | TIPOS DE DADOS E COLEÇÕES
import datetime   # Manipulação de data e hora.
import zoneinfo   # Suporte a fusos horários do mundo real.
import calendar   # Funções relacionadas ao calendário gregoriano.
import collections # Estruturas de dados (deque, Counter, OrderedDict, etc).
import bisect     # Manipulação de listas ordenadas (algoritmo de bisseção).
import heapq      # Algoritmo de fila de prioridade (heap).
import array      # Arrays eficientes de valores numéricos básicos.
import weakref    # Referências fracas (ajuda no gerenciamento de memória).
import types      # Nomes dinâmicos para tipos internos do Python.
import copy       # Operações de cópia rasa (shallow) e profunda (deep).
import pprint     # "Pretty-print": imprime estruturas de dados de forma legível.
import enum       # Suporte para enumerações.
# endregion

# region | MATEMÁTICA E NÚMEROS
import numbers    # Hierarquia de tipos numéricos.
import math       # Funções matemáticas (ponto flutuante).
import cmath      # Funções matemáticas para números complexos.
import decimal    # Aritmética decimal de precisão fixa e flutuante.
import fractions  # Números racionais (frações).
import random     # Gerador de números pseudo-aleatórios.
import statistics # Funções de estatística matemática.
# endregion

# region | ACESSO A ARQUIVOS E DIRETÓRIOS
import pathlib    # Caminhos de sistema de arquivos orientados a objetos.
import os.path    # Manipulações comuns de nomes de caminhos.
import stat       # Interpretando resultados de os.stat().
import filecmp    # Comparação de arquivos e diretórios.
import tempfile   # Geração de arquivos e diretórios temporários.
import glob       # Expansão de padrões de caminhos (tipo *.txt).
import fnmatch    # Comparação de nomes de arquivos no estilo Unix.
import linecache  # Acesso aleatório a linhas de arquivos de texto.
import shutil     # Operações de arquivos de alto nível (copy, move).
# endregion

# region | PERSISTÊNCIA DE DADOS
import pickle     # Serialização de objetos Python.
import copyreg    # Registro de funções de suporte para o pickle.
import shelve     # Persistência de objetos Python baseada em chave-valor.
import marshal    # Serialização interna de objetos do Python.
import dbm        # Interface para bancos de dados estilo DBM.
import sqlite3    # Interface para o banco de dados SQLite.
# endregion

# region | COMPRESSÃO E ARQUIVAMENTO
import zlib       # Compressão compatível com gzip.
import gzip       # Interface para arquivos .gz.
import bz2        # Interface para compressão bzip2.
import lzma       # Interface para compressão LZMA/XZ.
import zipfile    # Manipulação de arquivos .zip.
import tarfile    # Manipulação de arquivos .tar.
# endregion

# region | FORMATOS DE ARQUIVO E CRIPTOGRAFIA
import csv        # Leitura/Escrita de arquivos CSV.
import configparser # Manipulação de arquivos de configuração (.ini).
import tomllib    # Leitura de arquivos TOML (novo no Python 3.11).
import hashlib    # Algoritmos de hash (MD5, SHA-1, SHA-2 etc.); MD5 e SHA-1 são legados e não são adequados para usos criptográficos que dependam de resistência a colisões.
import hmac       # Autenticação de mensagens com hash (Keyed-Hashing).
import secrets    # Geração de segredos seguros para senhas/tokens.
# endregion

# region | SERVIÇOS DO SISTEMA OPERACIONAL
import os         # Interfaces genéricas do Sistema Operacional.
import io         # Ferramentas principais para lidar com I/O (streams).
import time       # Acesso e conversões de tempo.
import argparse   # Analisador de opções e argumentos de linha de comando.
import logging    # Facilidade de registro de eventos (logs).
import getpass    # Entrada de senha portátil.
import platform   # Acesso aos dados da plataforma subjacente.
import errno      # Símbolos de erro padrão do sistema.
import ctypes     # Biblioteca de funções estrangeiras (chama C no Python).
# endregion

# region | CONCORRÊNCIA E MULTIPROCESSAMENTO
import threading  # Gerenciamento de Threads.
import multiprocessing # Processamento paralelo baseado em processos.
import concurrent.futures # Lançador de tarefas paralelas de alto nível.
import subprocess # Gerenciamento de sub-processos (roda comandos externos).
import sched      # Agendador de eventos.
import queue      # Filas sincronizadas para comunicação entre threads; para processos, veja multiprocessing.Queue.
import asyncio    # I/O assíncrono (corrotinas).
# endregion

# region | REDE E COMUNICAÇÃO INTERPROCESSOS
import socket     # Interface de rede de baixo nível.
import ssl        # Wrapper TLS/SSL para sockets.
import select     # Espera por conclusão de I/O em múltiplos fluxos.
import selectors  # Multiplexação de I/O de alto nível.
import signal     # Manipulação de sinais para tratadores assíncronos.
import mmap       # Suporte a arquivos mapeados em memória.
# endregion

# region | PROTOCOLO INTERNET E SUPORTE A DADOS
import email      # Pacote de manipulação de e-mail e MIME.
import json       # Codificador e decodificador JSON.
import base64     # Codificações de dados binários em ASCII.
import binascii   # Conversões entre binário e ASCII.
import quopri     # Codificação e decodificação quoted-printable de MIME.
# endregion

# region | PROTOCOLO INTERNET (CLIENTES)
import urllib     # Módulos de manipulação de URLs.
import http       # Módulos HTTP (cliente e servidor).
import ftplib     # Cliente de protocolo FTP.
import poplib     # Cliente de protocolo POP3.
import imaplib    # Cliente de protocolo IMAP4.
import smtplib    # Cliente de protocolo SMTP.
import uuid       # Objetos identificadores únicos universais.

# NOTA DE VERSÃO (Python 3.13+):
# Os módulos abaixo foram REMOVIDOS na versão 3.13 por serem obsoletos:
# import nntplib   -> Removido
# import telnetlib -> Removido (Use bibliotecas externas como 'telnetlib3' se necessário)
# import cgi -> Removido
# endregion

# region | MULTIMÍDIA
import wave       # Leitura e escrita de arquivos WAV.
import colorsys   # Conversões entre sistemas de cores.
# endregion

# region | INTERFACE GRÁFICA
import tkinter    # Interface padrão Python para o kit de ferramentas Tcl/Tk.
# endregion

# region | FERRAMENTAS DE DESENVOLVIMENTO E DEBUG
import typing     # Suporte para dicas de tipo (Type Hints).
import pydoc      # Gerador de documentação e sistema de ajuda online.
import doctest    # Testa trechos de código em docstrings.
import unittest   # Framework de testes unitários.
import bdb        # Estrutura do depurador (debugger).
import pdb        # O depurador interativo do Python.
import timeit     # Mede o tempo de execução de pequenos trechos de código.
import trace      # Rastreia a execução de programas.
import tracemalloc # Rastreia alocações de memória.
# endregion

# region | RUNTIME DO PYTHON E SOFTWARE
import sys        # Parâmetros e funções específicas do sistema.
import gc         # Interface do coletor de lixo (Garbage Collector).
import inspect    # Inspeciona objetos vivos (classes, funções, etc).
import site       # Gerenciamento de configurações específicas de pacotes.
# endregion

# region | IMPORTAÇÃO E MÓDULOS
import importlib  # A implementação da instrução 'import'.
import zipimport  # Importar módulos de arquivos Zip.
import pkgutil    # Utilitários de suporte a pacotes.
import modulefinder # Localiza módulos usados por um script.
# endregion
