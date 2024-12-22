class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres.jymyxygdpomyecoiovdh:190720Ga@aws-0-us-west-1.pooler.supabase.com:6543/postgres'
    JWT_ALGORITHM = 'HS256'
    SECRET_KEY = '45419c82583e5ff0cbae613fd6'
    PROPAGATE_EXCEPTIONS = True # FUNCIONES DE TOKEN SE EJECUTAN AUTOMATICAMENTE