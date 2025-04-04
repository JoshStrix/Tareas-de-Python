PGDMP      
                }         
   esports_db    17.3    17.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    82005 
   esports_db    DATABASE     p   CREATE DATABASE esports_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en-US';
    DROP DATABASE esports_db;
                     postgres    false            �            1259    82006    equipos    TABLE     w   CREATE TABLE public.equipos (
    id integer NOT NULL,
    nombre text NOT NULL,
    pais text,
    entrenador text
);
    DROP TABLE public.equipos;
       public         heap r       postgres    false            �            1259    82016 	   jugadores    TABLE     �   CREATE TABLE public.jugadores (
    id integer NOT NULL,
    nickname text NOT NULL,
    rol text NOT NULL,
    equipo_id integer
);
    DROP TABLE public.jugadores;
       public         heap r       postgres    false            �            1259    82015    jugadores_id_seq    SEQUENCE     �   CREATE SEQUENCE public.jugadores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.jugadores_id_seq;
       public               postgres    false    219            �           0    0    jugadores_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.jugadores_id_seq OWNED BY public.jugadores.id;
          public               postgres    false    218            %           2604    82019    jugadores id    DEFAULT     l   ALTER TABLE ONLY public.jugadores ALTER COLUMN id SET DEFAULT nextval('public.jugadores_id_seq'::regclass);
 ;   ALTER TABLE public.jugadores ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    219    218    219            �          0    82006    equipos 
   TABLE DATA           ?   COPY public.equipos (id, nombre, pais, entrenador) FROM stdin;
    public               postgres    false    217   )       �          0    82016 	   jugadores 
   TABLE DATA           A   COPY public.jugadores (id, nickname, rol, equipo_id) FROM stdin;
    public               postgres    false    219   r       �           0    0    jugadores_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.jugadores_id_seq', 1, false);
          public               postgres    false    218            '           2606    82014    equipos equipos_nombre_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.equipos
    ADD CONSTRAINT equipos_nombre_key UNIQUE (nombre);
 D   ALTER TABLE ONLY public.equipos DROP CONSTRAINT equipos_nombre_key;
       public                 postgres    false    217            )           2606    82012    equipos equipos_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.equipos
    ADD CONSTRAINT equipos_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.equipos DROP CONSTRAINT equipos_pkey;
       public                 postgres    false    217            +           2606    82025     jugadores jugadores_nickname_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.jugadores
    ADD CONSTRAINT jugadores_nickname_key UNIQUE (nickname);
 J   ALTER TABLE ONLY public.jugadores DROP CONSTRAINT jugadores_nickname_key;
       public                 postgres    false    219            -           2606    82023    jugadores jugadores_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.jugadores
    ADD CONSTRAINT jugadores_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.jugadores DROP CONSTRAINT jugadores_pkey;
       public                 postgres    false    219            .           2606    82026 "   jugadores jugadores_equipo_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.jugadores
    ADD CONSTRAINT jugadores_equipo_id_fkey FOREIGN KEY (equipo_id) REFERENCES public.equipos(id) ON DELETE CASCADE;
 L   ALTER TABLE ONLY public.jugadores DROP CONSTRAINT jugadores_equipo_id_fkey;
       public               postgres    false    217    4649    219            �   9   x�34������L�L�2�t�J�-���t���I�t�+)J�KL�/RI-.����� doc      �      x������ � �     