import os

os.environ.setdefault('SECRET_KEY', 'eqG7DhJIhQfNsz0SJnbDg6sRXApgIDzX')

os.environ['DATABASE_URL'] = 'postgresql://neondb_owner:Dgitr6R0oyhV@ep-dark-bar-a2st7aof.eu-central-1.aws.neon.tech/shred_king_quail_26107'

os.environ['CLOUDINARY_CLOUD_NAME'] = 'dxwiahivd'
os.environ['CLOUDINARY_API_KEY'] = '371484113584354'
os.environ['CLOUDINARY_API_SECRET'] = 'EFP4_EqCcI3x2JwVqUqT44I2zsw'

os.environ.setdefault('STRIPE_PUBLIC_KEY', 'pk_test_51QqT2S07X5gc8qF8lYuwUIjV4CZIqfIiaJH0ZdfDdkjG5v2JEDUd0DqRjqhhHaYKNC9GPOklaj8NCxkPRDs9pBMY00EmjEzApq')
os.environ.setdefault('STRIPE_SECRET_KEY', 'sk_test_51QqT2S07X5gc8qF8DVvH7gK7BpgWePCsyvkS8Cc72ZoADSSwcBtJuMwasjNuqcOj62ppnFzlnS2QOgBu4BwvKfAY00s728lL4h')

os.environ.setdefault('STRIPE_WH_SECRET', 'whsec_50e7dcc12964b8a796d40ed9a645762498ee6d0bb561b8f6962fab0f665cf176')