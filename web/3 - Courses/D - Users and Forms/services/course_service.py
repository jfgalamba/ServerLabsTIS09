from decimal import Decimal as dec
from typing import List

from data.models import Course

def course_count() -> int:
    return 99
#:

def available_courses(count: int) -> List[Course]:
    return [
        Course(
            id = 1,
            category = 'Hotelaria e Turismo',
            price = dec(179),
            name = 'Gestor Turístico',
            summary = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            description = 'Non rem numquam debitis obcaecati unde repellendus, eaque eum est saepe accusamus molestias ipsa. Consectetur dicta fuga, fugiat veniam hic autem in cupiditate, non impedit nostrum porro! Corrupti aspernatur incidunt aliquam earum quis fugit soluta ad perspiciatis culpa eius dignissimos corporis vel optio recusandae, ipsum ullam libero id, ex harum cumque unde eveniet natus! Laboriosam voluptatem vel nemo facere non quidem officia, consequatur tenetur doloremque labore dolorum, corrupti dolore tempora ducimus!',
            trainer_id = 1,
            trainer_name = 'Osmar',
            schedule = 'Segundas e Quintas, 17 às 20h',
            available_seats = 40,
        ),
        Course(
            id = 2,
            category = 'Programação em C++',
            price = dec(250),
            name = 'Estruturas de Dados em C++',
            summary = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            description = ' Corrupti omnis maxime voluptatem sed nobis illo dolorum corporis est laboriosam molestiae, consectetur necessitatibus nihil delectus ea ullam obcaecati magnam? Sequi quis quae voluptates rerum obcaecati modi, qui molestias sit soluta recusandae aliquid non libero voluptas ipsam dicta numquam explicabo reprehenderit animi alias totam illo autem laborum a. Corrupti nam dicta, debitis et consequatur, explicabo distinctio incidunt cumque ab ullam eum sequi? Culpa?',
            trainer_id = 4,
            trainer_name = 'Bernardo',
            schedule = 'Terças e Quartas, 17h30 às 20h30',
            available_seats = 20,
        ),
        Course(
            id = 3,
            category = 'Natação',
            price = dec(250),
            name = 'Estilo Borboleta',
            summary = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            description = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut ab deserunt et vitae sunt, enim dolores beatae esse necessitatibus iusto. Error iure facere incidunt minima dolorum adipisci culpa! Maiores velit doloribus perferendis tempore, dicta est, sit necessitatibus commodi, sapiente minus quas. Vitae repellat quasi sunt, iusto atque pariatur! Suscipit sed maxime quaerat obcaecati accusamus neque nobis quidem, quisquam ducimus nemo illo corporis fugit eaque fugiat nisi, dolorum minima dignissimos, enim deserunt sint corrupti?',
            trainer_id = 2,
            trainer_name = 'Alberta',
            schedule = 'Terças e Sextas, 10 às 13h',
            available_seats = 16,
        ),
    ][:count]
#:

def most_popular_courses(count: int) -> List[Course]:
    return [
        Course(
            id = 1,
            category = 'Hotelaria e Turismo',
            price = dec(179),
            name = 'Gestor Turístico',
            summary = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            description = 'Non rem numquam debitis obcaecati unde repellendus, eaque eum est saepe accusamus molestias ipsa. Consectetur dicta fuga, fugiat veniam hic autem in cupiditate, non impedit nostrum porro! Corrupti aspernatur incidunt aliquam earum quis fugit soluta ad perspiciatis culpa eius dignissimos corporis vel optio recusandae, ipsum ullam libero id, ex harum cumque unde eveniet natus! Laboriosam voluptatem vel nemo facere non quidem officia, consequatur tenetur doloremque labore dolorum, corrupti dolore tempora ducimus!',
            trainer_id = 1,
            trainer_name = 'Osmar',
            schedule = 'Segundas e Quintas, 17 às 20h',
            available_seats = 40,
        ),
        Course(
            id = 2,
            category = 'Programação em C++',
            price = dec(250),
            name = 'Estruturas de Dados em C++',
            summary = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            description = ' Corrupti omnis maxime voluptatem sed nobis illo dolorum corporis est laboriosam molestiae, consectetur necessitatibus nihil delectus ea ullam obcaecati magnam? Sequi quis quae voluptates rerum obcaecati modi, qui molestias sit soluta recusandae aliquid non libero voluptas ipsam dicta numquam explicabo reprehenderit animi alias totam illo autem laborum a. Corrupti nam dicta, debitis et consequatur, explicabo distinctio incidunt cumque ab ullam eum sequi? Culpa?',
            trainer_id = 4,
            trainer_name = 'Bernardo',
            schedule = 'Terças e Quartas, 17h30 às 20h30',
            available_seats = 20,
        ),
        Course(
            id = 3,
            category = 'Natação',
            price = dec(250),
            name = 'Estilo Borboleta',
            summary = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            description = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut ab deserunt et vitae sunt, enim dolores beatae esse necessitatibus iusto. Error iure facere incidunt minima dolorum adipisci culpa! Maiores velit doloribus perferendis tempore, dicta est, sit necessitatibus commodi, sapiente minus quas. Vitae repellat quasi sunt, iusto atque pariatur! Suscipit sed maxime quaerat obcaecati accusamus neque nobis quidem, quisquam ducimus nemo illo corporis fugit eaque fugiat nisi, dolorum minima dignissimos, enim deserunt sint corrupti?',
            trainer_id = 2,
            trainer_name = 'Alberta',
            schedule = 'Terças e Sextas, 10 às 13h',
            available_seats = 16,
        ),
    ][:count]
#:

def get_course_by_id(course_id: int) -> Course | None:
    courses = available_courses(10000)
    for course in courses:
        if course.id == course_id:
            return course
    return None
#: