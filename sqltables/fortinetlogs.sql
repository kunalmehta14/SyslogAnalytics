-- public.devicelist definition

-- Drop table

-- DROP TABLE public.devicelist;

CREATE TABLE public.devicelist (
	devicename varchar(255) NULL,
	devid varchar(20) NOT NULL,
	devicevendor varchar(20) NULL,
	devip varchar(15) NOT NULL,
	CONSTRAINT devicelist_pk PRIMARY KEY (devip)
);
-- public.fortinetlogs definition

-- Drop table

-- DROP TABLE public.fortinetlogs;

CREATE TABLE public.fortinetlogs (
	logid varchar(50) NOT NULL,
	priority varchar(20) NULL,
	tz varchar(5) NULL,
	subtype varchar(20) NULL,
	vd varchar(50) NULL,
	srcip varchar(15) NULL,
	srcintf varchar(50) NULL,
	srcport int4 NULL,
	srcintfrole varchar(20) NULL,
	dstip varchar(15) NULL,
	dstintf varchar(50) NULL,
	dstport int4 NULL,
	dstintfrole varchar(15) NULL,
	srccountry varchar(50) NULL,
	dstcountry varchar(50) NULL,
	sessionid int8 NULL,
	proto int4 NULL,
	"action" varchar(15) NULL,
	policyid int4 NULL,
	policytype varchar(50) NULL,
	policyname varchar(50) NULL,
	service varchar(20) NULL,
	fortiuser varchar(50) NULL,
	fortigroup varchar(50) NULL,
	app varchar(50) NULL,
	authserver varchar(50) NULL,
	duration int4 NULL,
	sentbyte int8 NULL,
	rcvdbyte int8 NULL,
	sentpkt int8 NULL,
	rcvdpkt int8 NULL,
	vpntype varchar(20) NULL,
	dstmac varchar(20) NULL,
	dsthwvendor varchar(20) NULL,
	"timestamp" timestamp NOT NULL,
	"type" varchar(20) NULL,
	logdesc varchar(255) NULL,
	devip varchar(15) NULL,
	CONSTRAINT fortinetlogs_pk PRIMARY KEY (logid, "timestamp")
)
PARTITION BY RANGE ("timestamp");


-- public.fortinetlogs foreign keys

ALTER TABLE public.fortinetlogs ADD CONSTRAINT fortinetlogs_fk FOREIGN KEY (devip) REFERENCES public.devicelist(devip) ON DELETE CASCADE ON UPDATE CASCADE;