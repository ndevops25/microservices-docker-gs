# app.py - Microserviço de Produtos (versão simplificada)
from flask import Flask, jsonify, request

# Inicialização da aplicação Flask
app = Flask(__name__)

# Dados de exemplo
sample_products = [
    {
        "id": "prod-001",
        "name": "Smartphone XYZ",
        "description": "Smartphone de última geração com câmera de alta resolução",
        "price": 1999.99,# app.py - Microserviço de Avaliações (versão simplificada)
from flask import Flask, jsonify, request
from datetime import datetime

# Inicialização da aplicação Flask
app = Flask(__name__)

# Dados de exemplo
sample_reviews = [
    {
        "id": "rev-001",
        "product_id": "prod-001",
        "user_id": "user-001",
        "title": "Smartphone excelente!",
        "comment": "Comprei este smartphone e estou muito satisfeito. A câmera é incrível e a bateria dura o dia todo.",
        "rating": 5,
        "review_date": "2023-01-15T14:30:00",
        "photos": ["https://example.com/photos/review1-1.jpg", "https://example.com/photos/review1-2.jpg"],
        "helpfulness": {"likes": 12, "dislikes": 2},
        "status": "approved",
        "verified_purchase": True,
        "attributes": {"camera": 5, "battery": 4, "design": 5, "performance": 4}
    },
    {
        "id": "rev-002",
        "product_id": "prod-001",
        "user_id": "user-002",
        "title": "Bom, mas com alguns problemas",
        "comment": "O smartphone é bom, mas esquenta muito quando uso por muito tempo. A câmera é excelente!",
        "rating": 3,
        "review_date": "2023-02-20T10:15:00",
        "photos": [],
        "helpfulness": {"likes": 5, "dislikes": 1},
        "status": "approved",
        "verified_purchase": True,
        "attributes": {"camera": 5, "battery": 2, "design": 4, "performance": 3}
    },
    {
        "id": "rev-003",
        "product_id": "prod-002",
        "user_id": "user-003",
        "title": "Notebook perfeito para trabalho",
        "comment": "Comprei para trabalho e atendeu todas as expectativas. Rápido e com boa duração de bateria.",
        "rating": 5,
        "review_date": "2023-03-05T16:45:00",
        "photos": ["https://example.com/photos/review3-1.jpg"],
        "helpfulness": {"likes": 8, "dislikes": 0},
        "status": "approved",
        "verified_purchase": True,
        "attributes": {"performance": 5, "battery": 4, "design": 5, "keyboard": 4}
    },
    {
        "id": "rev-004",
        "product_id": "prod-003",
        "user_id": "user-004",
        "title": "Camiseta de boa qualidade",
        "comment": "O material é bom e não desbotou após várias lavagens. Recomendo!",
        "rating": 4,
        "review_date": "2023-02-28T09:30:00",
        "photos": [],
        "helpfulness": {"likes": 3, "dislikes": 0},
        "status": "approved",
        "verified_purchase": True,
        "attributes": {"quality": 4, "comfort": 5, "sizing": 4}
    },
    {
        "id": "rev-005",
        "product_id": "prod-001",
        "user_id": "user-005",
        "title": "Aguardando moderação",
        "comment": "Esta é uma avaliação que ainda não foi moderada.",
        "rating": 2,
        "review_date": "2023-03-10T11:20:00",
        "photos": [],
        "helpfulness": {"likes": 0, "dislikes": 0},
        "status": "pending",
        "verified_purchase": False,
        "attributes": {"camera": 2, "battery": 3, "design": 2, "performance": 2}
    }
]

# Respostas às avaliações
sample_responses = [
    {
        "id": "resp-001",
        "review_id": "rev-002",
        "user_id": "seller-001",
        "comment": "Agradecemos seu feedback. O aquecimento pode ocorrer em uso intenso. Sugerimos atualizar o software para a versão mais recente que melhorou este aspecto.",
        "response_date": "2023-02-22T14:30:00",
        "is_seller": True,
        "status": "active"
    },
    {
        "id": "resp-002",
        "review_id": "rev-003",
        "user_id": "user-006",
        "comment": "Concordo totalmente! Também uso para trabalho e é excelente.",
        "response_date": "2023-03-07T10:15:00",
        "is_seller": False,
        "status": "active"
    }
]

# Resumo de avaliações por produto
sample_summaries = {
    "prod-001": {
        "product_id": "prod-001",
        "average_rating": 4.0,
        "total_reviews": 3,
        "distribution": {"5": 1, "4": 0, "3": 1, "2": 1, "1": 0},
        "attribute_averages": {"camera": 4.0, "battery": 3.0, "design": 3.67, "performance": 3.0},
        "last_updated": "2023-03-10T11:20:00"
    },
    "prod-002": {
        "product_id": "prod-002",
        "average_rating": 5.0,
        "total_reviews": 1,
        "distribution": {"5": 1, "4": 0, "3": 0, "2": 0, "1": 0},
        "attribute_averages": {"performance": 5.0, "battery": 4.0, "design": 5.0, "keyboard": 4.0},
        "last_updated": "2023-03-05T16:45:00"
    },
    "prod-003": {
        "product_id": "prod-003",
        "average_rating": 4.0,
        "total_reviews": 1,
        "distribution": {"5": 0, "4": 1, "3": 0, "2": 0, "1": 0},
        "attribute_averages": {"quality": 4.0, "comfort": 5.0, "sizing": 4.0},
        "last_updated": "2023-02-28T09:30:00"
    }
}

# Informações dos produtos (adicionando esta estrutura para suportar as novas funções)
sample_products = {
    "prod-001": {
        "id": "prod-001",
        "name": "Smartphone Galaxy X10",
        "category": "Eletrônicos",
        "price": 2499.90,
        "brand": "Samsung",
        "description": "Smartphone com tela AMOLED de 6.5\", 128GB de armazenamento e 8GB de RAM"
    },
    "prod-002": {
        "id": "prod-002",
        "name": "Notebook ProBook Ultra",
        "category": "Informática",
        "price": 4899.90,
        "brand": "HP",
        "description": "Notebook com processador Intel i7, 16GB de RAM e SSD de 512GB"
    },
    "prod-003": {
        "id": "prod-003",
        "name": "Camiseta Casual Básica",
        "category": "Vestuário",
        "price": 79.90,
        "brand": "Essentials",
        "description": "Camiseta 100% algodão, corte regular, disponível em várias cores"
    }
}

# Rotas do microserviço

@app.route('/avaliacoes/produtos/<product_id>', methods=['GET'])
def get_product_reviews(product_id):
    """
    Retorna as avaliações de um produto
    """
    # Parâmetros opcionais
    status = request.args.get('status', 'approved')  # Por padrão, retorna apenas aprovadas
    
    # Filtra as avaliações
    if status == 'all':
        reviews = [r for r in sample_reviews if r['product_id'] == product_id]
    else:
        reviews = [r for r in sample_reviews if r['product_id'] == product_id and r['status'] == status]
    
    # Para cada avaliação, adiciona suas respostas
    reviews_with_responses = []
    for review in reviews:
        review_data = dict(review)
        review_data['responses'] = [r for r in sample_responses if r['review_id'] == review['id'] and r['status'] == 'active']
        reviews_with_responses.append(review_data)
    
    return jsonify({
        'reviews': reviews_with_responses,
        'total': len(reviews_with_responses),
        'product_id': product_id
    })

# Rota para verificar a saúde do serviço
@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint para verificação de saúde do serviço
    """
    return jsonify({'status': 'ok', 'service': 'avaliações'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)
        "stock": 50,
        "category_id": "cat-002",
        "supplier_id": "sup-001",
        "features": {
            "color": "Preto",
            "memory": "128GB",
            "screen": "6.5 polegadas"
        },
        "images": ["https://example.com/images/phone1.jpg", "https://example.com/images/phone2.jpg"],
        "status": "active",
        "sku": "PHONE-XYZ-128"
    },
    {
        "id": "prod-002",
        "name": "Notebook ABC",
        "description": "Notebook leve e potente para trabalho",
        "price": 4500.00,
        "stock": 20,
        "category_id": "cat-001",
        "supplier_id": "sup-002",
        "features": {
            "color": "Prata",
            "memory": "16GB RAM",
            "processor": "Intel Core i7",
            "storage": "512GB SSD"
        },
        "images": ["https://example.com/images/laptop1.jpg"],
        "status": "active",
        "sku": "NOTE-ABC-16"
    },
    {
        "id": "prod-003",
        "name": "Camiseta Casual",
        "description": "Camiseta de algodão confortável",
        "price": 59.90,
        "stock": 100,
        "category_id": "cat-003",
        "supplier_id": "sup-003",
        "features": {
            "color": "Azul",
            "size": "M",
            "material": "100% Algodão"
        },
        "images": ["https://example.com/images/tshirt1.jpg"],
        "status": "active",
        "sku": "SHIRT-CASUAL-M"
    }
]

# Histórico de preços simulado
sample_price_history = {
    "prod-001": [
        {"previous_price": 2199.99, "new_price": 1999.99, "change_date": "2023-01-15", "reason": "Promoção de Verão"},
        {"previous_price": 2299.99, "new_price": 2199.99, "change_date": "2022-11-20", "reason": "Black Friday"}
    ],
    "prod-002": [
        {"previous_price": 4799.00, "new_price": 4500.00, "change_date": "2023-02-10", "reason": "Ajuste de Mercado"}
    ]
}

# Rotas do microserviço

@app.route('/produtos', methods=['GET'])
def get_all_products():
    """
    Retorna todos os produtos
    """
    return jsonify([{
        'id': product['id'],
        'name': product['name'],
        'price': product['price'],
        'stock': product['stock'],
        'category_id': product['category_id'],
        'supplier_id': product['supplier_id'],
        'status': product['status']
    } for product in sample_products])

@app.route('/produtos/<product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retorna um produto específico pelo ID
    """
    product = next((p for p in sample_products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Produto não encontrado'}), 404

# Rota para verificar a saúde do serviço
@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint para verificação de saúde do serviço
    """
    return jsonify({'status': 'ok', 'service': 'produtos'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6004)