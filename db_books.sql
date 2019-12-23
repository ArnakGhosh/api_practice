--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.4
-- Dumped by pg_dump version 9.5.4

-- Started on 2019-12-23 11:52:57

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 204 (class 1259 OID 874906)
-- Name: books; Type: TABLE; Schema: public; Owner: pytest
--

CREATE TABLE books (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    author character varying(100) NOT NULL,
    first_sentence character varying(400) NOT NULL,
    published character varying(6) NOT NULL
);


ALTER TABLE books OWNER TO pytest;

--
-- TOC entry 2157 (class 0 OID 874906)
-- Dependencies: 204
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: pytest
--

INSERT INTO books (id, title, author, first_sentence, published) VALUES (0, 'A Fire Upon the Deep', 'Vernor Vinge', 'The coldsleep itself was dreamless.', '1992');
INSERT INTO books (id, title, author, first_sentence, published) VALUES (2, 'Dhalgren', 'Samuel R. Delany', 'to wound the autumnal city.', '1975');
INSERT INTO books (id, title, author, first_sentence, published) VALUES (3, 'A Matchbox Full Of Dreams', 'Edward Dutta', 'Never lie under the shadow of your dreams, until you set yourself free, with no strings attached.', '1975');
INSERT INTO books (id, title, author, first_sentence, published) VALUES (1, 'The Ones Who Walk Away From Omelas', 'Ursula K. Le Guin', 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', '1973');


--
-- TOC entry 2042 (class 2606 OID 874910)
-- Name: books_pkey; Type: CONSTRAINT; Schema: public; Owner: pytest
--

ALTER TABLE ONLY books
    ADD CONSTRAINT books_pkey PRIMARY KEY (id);


-- Completed on 2019-12-23 11:52:58

--
-- PostgreSQL database dump complete
--

