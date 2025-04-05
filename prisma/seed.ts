import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

async function main() {
  await prisma.user.create({
    data: {
      email: "test@example.com",
      password: "hashedpassword"
    }
  });
}

main()
  .catch(e => console.error(e))
  .finally(() => prisma.$disconnect());
