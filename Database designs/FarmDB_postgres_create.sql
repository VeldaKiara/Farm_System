CREATE TABLE "Farmer" (
	"id" serial NOT NULL,
	"name" varchar(255) NOT NULL,
	"email" varchar(255) NOT NULL,
	"gender" varchar(255) NOT NULL,
	"fertilizers" varchar(255) NOT NULL,
	"equipment" varchar(255) NOT NULL,
	"products" varchar(255) NOT NULL,
	"pesticides" varchar(255) NOT NULL,
	CONSTRAINT "Farmer_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Consumer" (
	"id" serial NOT NULL,
	"name" serial(255) NOT NULL,
	"email" serial(255) NOT NULL,
	"gender" serial(255) NOT NULL,
	CONSTRAINT "Consumer_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Equipment" (
	"Machinery" varchar(255) NOT NULL,
	"Tools" varchar(255) NOT NULL,
	"id" serial(255) NOT NULL,
	CONSTRAINT "Equipment_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "pesticides" (
	"id" serial NOT NULL,
	"category" varchar(255) NOT NULL,
	CONSTRAINT "pesticides_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "fertilizers" (
	"id" serial NOT NULL,
	"category" serial(255) NOT NULL,
	CONSTRAINT "fertilizers_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Products" (
	"id" serial NOT NULL,
	"category" serial(255) NOT NULL,
	CONSTRAINT "Products_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "grains" (
	"id" serial(255) NOT NULL,
	"name" varchar(255) NOT NULL,
	"category" varchar(255) NOT NULL,
	CONSTRAINT "grains_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "fruits" (
	"id" serial(255) NOT NULL,
	"name" varchar(255) NOT NULL,
	"category" varchar(255) NOT NULL,
	CONSTRAINT "fruits_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "vegetables" (
	"id" serial(255) NOT NULL,
	"name" varchar(255) NOT NULL,
	"category" varchar(255) NOT NULL,
	CONSTRAINT "vegetables_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "dairy" (
	"id" serial(255) NOT NULL,
	"name" varchar(255) NOT NULL,
	"category" varchar(255) NOT NULL,
	CONSTRAINT "dairy_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



ALTER TABLE "Farmer" ADD CONSTRAINT "Farmer_fk0" FOREIGN KEY ("fertilizers") REFERENCES "fertilizers"("id");
ALTER TABLE "Farmer" ADD CONSTRAINT "Farmer_fk1" FOREIGN KEY ("equipment") REFERENCES "Equipment"("id");
ALTER TABLE "Farmer" ADD CONSTRAINT "Farmer_fk2" FOREIGN KEY ("products") REFERENCES "Products"("id");
ALTER TABLE "Farmer" ADD CONSTRAINT "Farmer_fk3" FOREIGN KEY ("pesticides") REFERENCES "pesticides"("id");


ALTER TABLE "Equipment" ADD CONSTRAINT "Equipment_fk0" FOREIGN KEY ("Machinery") REFERENCES "Machinery"("id");
ALTER TABLE "Equipment" ADD CONSTRAINT "Equipment_fk1" FOREIGN KEY ("Tools") REFERENCES "Tools"("id");




ALTER TABLE "grains" ADD CONSTRAINT "grains_fk0" FOREIGN KEY ("category") REFERENCES "Products"("id");

ALTER TABLE "fruits" ADD CONSTRAINT "fruits_fk0" FOREIGN KEY ("category") REFERENCES "Products"("id");

ALTER TABLE "vegetables" ADD CONSTRAINT "vegetables_fk0" FOREIGN KEY ("category") REFERENCES "Products"("id");

ALTER TABLE "dairy" ADD CONSTRAINT "dairy_fk0" FOREIGN KEY ("category") REFERENCES "Products"("id");

