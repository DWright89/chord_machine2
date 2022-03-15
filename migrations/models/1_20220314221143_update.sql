-- upgrade --
ALTER TABLE "users" ADD "name" TEXT NOT NULL;
-- downgrade --
ALTER TABLE "users" DROP COLUMN "name";
