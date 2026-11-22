from django.shortcuts import render

data = [
    {
        'id': 1,
        'title': 'Beautiful India',
        'desc': 'Jammu and Kashmir is a beautiful region in northern India, renowned for its breathtaking landscapes, snow-capped mountains, lush green valleys, crystal-clear lakes, and picturesque gardens. Often referred to as Paradise on Earth, it is home to magnificent destinations such as Srinagar, Gulmarg, Pahalgam, and Dal Lake. Visitors can enjoy scenic houseboat rides, explore beautiful Mughal gardens, experience snowfall, and admire the stunning natural beauty of the Himalayas. Jammu and Kashmir offers an unforgettable experience for nature lovers, adventure seekers, and travellers.',
        'pic': 'https://images.unsplash.com/photo-1643449416258-5c8e7ec598b1?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D',
        'pic2': 'https://images.unsplash.com/photo-1542003488933-7cfa7453807a?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },

    {
        'id': 2,
        'title': 'Gorgeous Nepal',
        'desc': 'Nepal is a beautiful country known for its majestic Himalayan mountains, breathtaking landscapes, peaceful valleys, and rich cultural heritage. Home to Mount Everest, the highest peak in the world, Nepal attracts adventure seekers and nature lovers from across the globe. Visitors can explore Kathmandu, admire the beautiful lakes of Pokhara, experience mountain trekking, and discover ancient temples and traditions. Nepal offers an unforgettable combination of natural beauty, adventure, and spirituality.',
        'pic': 'https://images.unsplash.com/photo-1764140608148-80e010804af8?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D',
        'pic2': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaVvEZwmm66-s7J8F2XSMTwZaPD1loPkV7ean2LPye8w&s=10'
    },

    {
        'id': 3,
        'title': 'Attractive Japan',
        'desc': 'Kyoto is one of Japan’s most beautiful cities, famous for its traditional temples, peaceful gardens, cherry blossoms, and historic streets. The city offers a wonderful combination of ancient Japanese culture and natural beauty. Tourists visit Kyoto to experience its beautiful architecture, traditional tea houses, and colourful seasonal landscapes.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSu8sW6XrSWjFqknhJWijYDYAEnlrbarZ3QGnNf9A0IDA&s=10',
        'pic2': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLuXsvcPaRvN-T3tFoOQtlJOTUSYelrA4IPvJOW2FWFg&s=10'
    },

    {
        'id': 4,
        'title': 'Dreamy Maldives',
        'desc': 'The Maldives is a tropical paradise located in the Indian Ocean. It is famous for its crystal-clear blue waters, white sandy beaches, luxurious resorts, and colourful marine life. The beautiful islands are perfect for relaxing, swimming, diving, and enjoying breathtaking ocean views.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUR4X7LsSY8jGREbKv4xJKUGMhf5a6eex25q_4nqsByg&s=10',
        'pic2': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSq9InorkGRMtfGSaThSPTLTTs7qwQPB6RuXVfA0LG7Q&s=10'
    },

    {
        'id': 5,
        'title': 'Amazing Singapore',
        'desc': 'Singapore is a modern and beautiful city known for its impressive skyline, clean streets, lush gardens, and world-famous attractions. Gardens by the Bay, Marina Bay Sands, and Sentosa Island are some of its most popular tourist destinations. Singapore combines modern architecture with greenery and cultural diversity.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7iQguCyM8Fld-TpGl698CDs2OW7JmibjknvP2WnJ2Ig&s=10',
        'pic2': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiXxsqiXUh5K8hSAhDJPSvqIDZf9goJtQ4UkgVmV5NqQ&s=10'
    },

    {
        'id': 6,
        'title': 'Stunning Thailand',
        'desc': 'Thailand is a wonderful Asian destination known for its tropical beaches, magnificent temples, vibrant cities, and delicious cuisine. Places such as Phuket, Bangkok, and Krabi attract tourists with their beautiful landscapes, cultural attractions, and exciting activities. Thailand offers a perfect combination of adventure, relaxation, and cultural experiences.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRD2l84wZktWh8LExnPWDKy6zO605x-XYIgYjQ9jYn7BQ&s=10',
        'pic2': 'https://plus.unsplash.com/premium_photo-1693149386423-2e4e264712e5?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    }
]

data2 = [
    {
        'id': 7,
        'title': 'Beautiful Paris',
        'desc': 'Paris, the capital of France, is one of the most beautiful and romantic cities in the world. Famous for the Eiffel Tower, Louvre Museum, Notre-Dame Cathedral, and charming streets, Paris attracts millions of tourists every year. The city is known for its magnificent architecture, art, fashion, delicious cuisine, and breathtaking views. Visitors can enjoy peaceful walks along the Seine River, explore beautiful gardens, and experience the unique charm of French culture. Paris offers an unforgettable experience filled with elegance, history, and beauty.',
        'pic': 'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D',
        'pic2': 'https://media.istockphoto.com/id/635758088/photo/sunrise-at-the-eiffel-tower-in-paris-along-the-seine.webp?a=1&b=1&s=612x612&w=0&k=20&c=o6ycGpPSqeT6H3To6y7WFsZ0BLUEB3TKVtkHORQPGSY='
    },

    {
        'id': 8,
        'title': 'Magical Switzerland',
        'desc': 'Switzerland is a breathtaking European country famous for its snow-covered mountains, crystal-clear lakes, green valleys, and picturesque villages. The Swiss Alps offer spectacular views and are popular for skiing, hiking, and other outdoor adventures. Destinations such as Interlaken, Lucerne, and Zermatt attract visitors from around the world. Switzerland is also known for its beautiful railway journeys, peaceful surroundings, delicious chocolates, and charming landscapes. It is a perfect destination for nature lovers and travellers seeking a memorable holiday.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTa8a6WbNPfKPi7sKbdomoitwXwjcGEoxTsGS63p0Pg8Q&s=10',
        'pic2': 'https://images.unsplash.com/photo-1521292270410-a8c4d716d518?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },

    {
        'id': 9,
        'title': 'Attractive Netherlands',
        'desc': 'The Netherlands is a charming European country known for its colourful tulip fields, beautiful canals, windmills, and picturesque villages. Amsterdam, its capital, is famous for its historic buildings, museums, cycling culture, and peaceful waterways. During spring, the country transforms into a colourful paradise filled with blooming tulips. Visitors can explore traditional windmills, enjoy boat rides along canals, and experience the beauty of Dutch culture. The Netherlands offers a wonderful combination of modern cities, natural beauty, and rich history.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ42R7cJtgifTV2U6FDALIQhsmdCCpPhrqHhXflmcsUfw&s=10',
        'pic2': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjLmbcw8wLMhN-3dieP1tb8ALtt_FVnyAzpuak25D6Hg&s=10'
    },

    {
        'id': 10,
        'title': 'Enchanting Italy',
        'desc': 'Italy is a fascinating European destination famous for its rich history, magnificent architecture, beautiful coastlines, and delicious cuisine. Rome is home to iconic landmarks such as the Colosseum and the Trevi Fountain, while Venice is known for its romantic canals and gondola rides. Florence showcases stunning Renaissance art and architecture, and the Amalfi Coast offers breathtaking seaside views. Italy combines ancient history, artistic treasures, beautiful cities, and unforgettable experiences, making it one of the most popular tourist destinations in the world.',
        'pic': 'https://plus.unsplash.com/premium_photo-1675975678457-d70708bf77c8?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D',
        'pic2': 'https://images.unsplash.com/photo-1785014413554-e3fdc6e89ae4?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },

    {
        'id': 11,
        'title': 'Wonderful Finland',
        'desc': 'Finland is a beautiful Nordic country known for its peaceful forests, thousands of lakes, snowy landscapes, and stunning natural beauty. During winter, visitors can experience magical snow-covered scenery and witness the spectacular Northern Lights, especially in Lapland. Finland is also famous for its cosy cabins, saunas, and unique Arctic experiences. In summer, the country becomes a paradise of greenery, lakes, and endless daylight. Finland offers a peaceful escape for travellers who love nature, adventure, and beautiful landscapes.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTM2m9Mjkxj-ANxrDcZ4agGHz6X7YBSeK5LewqwSaPTQA&s=10',
        'pic2': 'https://plus.unsplash.com/premium_photo-1742493639933-4eeb46df59af?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },


    {
        'id': 12,
        'title': 'Dreamy Norway',
        'desc': 'Norway is a spectacular country known for its dramatic fjords, towering mountains, beautiful waterfalls, and breathtaking natural landscapes. The Norwegian fjords are among the most stunning attractions in Europe, offering unforgettable views of deep blue waters surrounded by mountains. Cities such as Oslo and Bergen combine modern architecture with rich cultural heritage. Visitors can enjoy scenic cruises, hiking adventures, and the magical Northern Lights during winter. Norway is a perfect destination for travellers who love nature, peaceful surroundings, and extraordinary scenery.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpplKx1JM8m1_4OldvkZij5_t27TqSa0MRqbmcX64v9w&s=10',
        'pic2': 'https://images.unsplash.com/photo-1544009520-e2ea9189f15e?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    }
]

data3 = [
    {
        'id': 13,
        'title': 'Beautiful Canberra',
        'desc': 'Canberra is the capital city of Australia and is known for its beautiful landscapes, modern architecture, and peaceful surroundings. The city is home to important national landmarks, museums, galleries, and government buildings. Lake Burley Griffin adds to the beauty of Canberra, offering scenic views and opportunities for boating, cycling, and relaxing by the waterfront. Surrounded by nature and greenery, Canberra is a wonderful destination for visitors interested in history, culture, and beautiful city landscapes.',
        'pic': 'https://media.istockphoto.com/id/1173722079/photo/canberra-act-australia.webp?a=1&b=1&s=612x612&w=0&k=20&c=6MrMxhQ3h50xdAnsnp78ZP5JccIbUmbNd-I8MhluGf4=',
        'pic2': 'https://media.istockphoto.com/id/498431528/photo/canberra-australia-at-dusk.webp?a=1&b=1&s=612x612&w=0&k=20&c=FiogyE4LfkvboDnRXAVRK1BXC8APXi61x_bw2ifHcw0='
    },

    {
        'id': 14,
        'title': 'Vibrant Brisbane',
        'desc': 'Brisbane is a beautiful city in Australia known for its warm climate, stunning river views, and vibrant atmosphere. The city is surrounded by natural beauty and offers attractions such as South Bank Parklands, Brisbane River, and the famous Story Bridge. Visitors can enjoy river cruises, beautiful gardens, outdoor activities, and lively cultural experiences. Brisbane combines modern city life with a relaxed atmosphere, making it a wonderful destination for travellers.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxTiKdDTQYLGt3EWbCPBB6-Pztkg35xi2v9iDHL9Nc0g&s=10',
        'pic2': 'https://images.unsplash.com/photo-1789758489945-cc32844a0382?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDE%3D'
    },

    {
        'id': 15,
        'title': 'Wonderful Melbourne',
        'desc': 'Melbourne is one of Australia’s most beautiful and vibrant cities, famous for its artistic culture, stunning architecture, colourful street art, and lively atmosphere. The city is known for its charming laneways, cafés, gardens, and cultural attractions. Visitors can explore Federation Square, the Royal Botanic Gardens, and the beautiful waterfront. Melbourne offers a perfect blend of modern city life, creativity, nature, and cultural experiences, making it a popular destination for tourists.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiJ0dMwMckVCiZrtxRTitlc1G1rnFL00RNPFnxT8kv3g&s=10',
        'pic2': 'https://images.unsplash.com/photo-1637402005822-d66b3c732d2a?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },

    {
        'id': 16,
        'title': 'Stunning Sydney',
        'desc': 'Sydney is one of the most iconic cities in Australia, renowned for its magnificent harbour, beautiful beaches, and world-famous landmarks. The Sydney Opera House and Harbour Bridge are among the most recognisable attractions in the world. Visitors can enjoy breathtaking views of the harbour, relax at Bondi Beach, explore the city’s vibrant streets, and experience its lively cultural scene. Sydney offers a perfect combination of natural beauty, modern architecture, and unforgettable travel experiences.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-Z37joGUDDrzB1roDiSIoXju_rXTaSWXN9o7SjxWRUA&s=10',
        'pic2': 'https://images.unsplash.com/photo-1624138784614-87fd1b6528f8?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },

    {
        'id': 17,
        'title': 'Amazing New South Wales',
        'desc': 'New South Wales is a beautiful state in Australia known for its diverse landscapes, stunning beaches, magnificent mountains, and charming countryside. From the vibrant city of Sydney to the peaceful coastal towns and picturesque valleys, the state offers countless destinations to explore. Visitors can enjoy beautiful national parks, scenic coastal drives, waterfalls, wildlife, and outdoor adventures. New South Wales is a wonderful destination for travellers seeking natural beauty, relaxation, and exciting experiences.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMpOKbC2zSsm01LJiVaM-L5s2uLm-Y_0P9igF59r6hXQ&s=10',
        'pic2': 'https://images.unsplash.com/photo-1779631864941-164f14ef9fcf?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },

    {
        'id': 18,
        'title': 'Breathtaking Snowy Mountains',
        'desc': 'The Snowy Mountains are one of Australia’s most spectacular natural destinations, famous for their snow-covered peaks, alpine landscapes, and breathtaking scenery. Located in New South Wales, the region is home to Mount Kosciuszko, the highest mountain in Australia. During winter, visitors can enjoy skiing, snowboarding, and other snow activities, while summer offers beautiful hiking trails, lakes, and scenic views. The Snowy Mountains are a perfect destination for adventure seekers and nature lovers.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRonYnUdSSejNYpQ-3MF0eDuJa8neurvk6QtsxY7NrIEA&s=10',
        'pic2': 'https://images.unsplash.com/photo-1729400860940-e6c122f32439?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    }
]

data4 = [
    {
        'id': 19,
        'title': 'Beautiful Butchart Gardens',
        'desc': 'Butchart Gardens, located in British Columbia, is one of the most beautiful gardens in Canada. It is famous for its colourful flowers, beautifully designed landscapes, peaceful pathways, and stunning floral displays. The garden features different themed areas, including the Sunken Garden, Rose Garden, Japanese Garden, and Italian Garden. Visitors can enjoy breathtaking views of blooming flowers, fountains, and lush greenery throughout the year. Butchart Gardens is a wonderful destination for nature lovers and those seeking a peaceful and relaxing experience.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1qm65rgWVj1MZf3uUamXeTj5udXQhPYzmcwpFJBE85g&s=10',
        'pic2': 'https://images.unsplash.com/photo-1558449709-9215b1ec91de?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },

    {
        'id': 20,
        'title': 'Enchanting Montreal Botanical Garden',
        'desc': 'The Montreal Botanical Garden is one of the largest and most beautiful botanical gardens in the world. Located in Quebec, it features an impressive collection of plants, flowers, trees, and themed gardens. Visitors can explore the Chinese Garden, Japanese Garden, Rose Garden, and many other beautiful sections. The garden is known for its colourful seasonal displays, peaceful atmosphere, and stunning landscapes. It is a perfect destination for nature lovers, photographers, and visitors who enjoy exploring beautiful gardens.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsaKWg8FYKHEbiR4gK0eNO9t47C6Wj5EylZUXRtB9XjQ&s=10',
        'pic2': 'https://images.unsplash.com/photo-1786471535952-2975a56a3e91?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },

    {
        'id': 21,
        'title': 'Stunning Vancouver',
        'desc': 'Vancouver is one of Canada’s most beautiful cities, surrounded by mountains, forests, and the Pacific Ocean. It is famous for its stunning waterfront, modern skyline, beautiful parks, and scenic beaches. Stanley Park, Granville Island, and the Vancouver Seawall are some of its popular attractions. Visitors can enjoy breathtaking views, outdoor activities, shopping, and cultural experiences. Vancouver offers a wonderful combination of urban life and natural beauty, making it a popular destination for travellers.',
        'pic': 'https://images.unsplash.com/photo-1660143158587-bddffa026e06?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D',
        'pic2': 'https://images.unsplash.com/photo-1780212575096-753ea517f8c4?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },

    {
        'id': 22,
        'title': 'Amazing Toronto',
        'desc': 'Toronto is Canada’s largest city and one of its most vibrant destinations. It is famous for its impressive skyline, multicultural atmosphere, beautiful waterfront, and iconic CN Tower. Visitors can explore museums, art galleries, shopping districts, parks, and exciting entertainment attractions. The city offers breathtaking views of Lake Ontario and is known for its diverse cultures, delicious food, and lively atmosphere. Toronto is a wonderful destination for travellers who enjoy modern cities and unforgettable experiences.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5IrHVTgPPwpgBZ1-YhziL1CU3egYMx0638kEm3MzpGA&s=10',
        'pic2': 'https://plus.unsplash.com/premium_photo-1694475611884-0424c49f2676?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },

    {
        'id': 23,
        'title': 'Rocky Mountains',
        'desc': 'The Canadian Rocky Mountains are among the most spectacular natural wonders in the world. Famous for their towering rocky peaks, crystal-clear lakes, deep valleys, and breathtaking landscapes, the Rockies attract nature lovers and adventure seekers from across the globe. Banff National Park and Jasper National Park are popular destinations where visitors can enjoy hiking, camping, wildlife spotting, and scenic drives. The magnificent mountains and turquoise lakes create unforgettable views and make the Canadian Rockies a truly extraordinary destination.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTldNDy1CCSknVZeBsEoHFiAKpbjpnQq8qpUr8bBvrGkg&s=10',
        'pic2': 'https://images.unsplash.com/photo-1587381419916-78fc843a36f8?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },

    {
        'id': 24,
        'title': 'Snowy Wonderland',
        'desc': 'Whistler is a breathtaking mountain destination in British Columbia, Canada, famous for its snow-covered landscapes, towering peaks, and world-class ski resorts. During winter, the region transforms into a magical snowy wonderland where visitors can enjoy skiing, snowboarding, snowshoeing, and other winter activities. The beautiful mountain scenery, frozen lakes, and charming village atmosphere make Whistler a popular destination for travellers. It offers an unforgettable experience for those who love snow, adventure, and stunning winter landscapes.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvub-R46S-xLpWIg395nyoSgUhj4ww7hJicdbEoFOHkA&s=10',
        'pic2': 'https://plus.unsplash.com/premium_photo-1669868118352-850ff89778b3?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    }
]

data5 = [
    {
        'id': 25,
        'title': 'Majestic Mount Kilimanjaro',
        'desc': 'Mount Kilimanjaro in Tanzania is the highest mountain in Africa and one of the most spectacular natural wonders of the continent. Its snow-covered peaks, breathtaking landscapes, and diverse ecosystems attract adventure seekers and nature lovers from around the world. The mountain offers a remarkable journey through forests, alpine deserts, and glaciers, making it a dream destination for trekking enthusiasts.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOXbi8n23Qi6ar-vO-MSxmyEmACXXz43BIh1i4VZJ8KQ&s=10',
        'pic2': 'https://images.unsplash.com/photo-1489392191049-fc10c97e64b6?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },

    {
        'id': 26,
        'title': 'Beautiful Seychelles',
        'desc': 'Seychelles is a stunning island destination known for its crystal-clear turquoise waters, white sandy beaches, lush tropical forests, and unique granite rock formations. The islands offer a peaceful atmosphere and breathtaking coastal scenery. Visitors can enjoy swimming, snorkelling, relaxing on beautiful beaches, and exploring the rich marine life. Seychelles is a perfect destination for travellers seeking tropical beauty and relaxation.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSF72H8eYKqvzlqVnCUosi9qzErgC3DGQ4TsuNw8shR2g&s=10',
        'pic2': 'https://images.unsplash.com/photo-1553829176-61484f865ac3?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },

    {
        'id': 27,
        'title': 'Amazing Sahara Desert',
        'desc': 'The Sahara Desert is the largest hot desert in the world, famous for its endless golden sand dunes, vast landscapes, and spectacular sunsets. Its beautiful scenery creates a unique and unforgettable experience for travellers. Visitors can explore the desert through camel rides, enjoy peaceful desert camps, admire the star-filled night sky, and experience the fascinating culture of the surrounding regions.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_SHCrvs1y5xFkU1A67oLNtDg28lmQNAuDD6nIOzIrAw&s=10',
        'pic2': 'https://images.unsplash.com/photo-1613169620329-6785c004d900?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },

    {
        'id': 28,
        'title': 'Beautiful Victoria Falls',
        'desc': 'Victoria Falls is one of the most spectacular waterfalls in the world, located on the border between Zambia and Zimbabwe. The enormous waterfall creates a breathtaking sight as millions of litres of water plunge into the gorge below. Surrounded by lush greenery and misty landscapes, it offers stunning views and exciting adventure activities. Victoria Falls is a remarkable destination for nature lovers and travellers.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2ed4GihTfX0sRm4zrrH6bFfbiQJBHyhL4mJK1ZE76qg&s=10',
        'pic2': 'https://plus.unsplash.com/premium_photo-1697729979889-31ec7ecf6f06?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },

    {
        'id': 29,
        'title': 'Vibrant Marrakech',
        'desc': 'Marrakech in Morocco is a beautiful city known for its colourful architecture, traditional markets, stunning gardens, and rich cultural heritage. The city offers a fascinating blend of ancient traditions and modern attractions. Visitors can explore the famous souks, admire magnificent palaces, enjoy traditional Moroccan cuisine, and experience the lively atmosphere of its streets. Marrakech is a wonderful destination for travellers seeking culture, history, and unforgettable experiences.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRMWMnSTABpVY_5kMtJDUmRMalBImBpymkf_hoqtAYDg&s=10',
        'pic2': 'https://images.unsplash.com/photo-1597212618440-806262de4f6b?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    },

    {
        'id': 30,
        'title': 'Beautiful Cape Town',
        'desc': 'Cape Town is one of the most beautiful cities in South Africa, famous for its stunning beaches, breathtaking ocean views, and magnificent Table Mountain. The city offers a wonderful combination of natural beauty, modern architecture, vibrant culture, and historical attractions. Visitors can explore the colourful Bo-Kaap neighbourhood, enjoy scenic cable car rides to Table Mountain, relax at beautiful beaches, and admire spectacular sunsets along the coastline. Cape Town is a perfect destination for travellers seeking unforgettable experiences surrounded by natural beauty.',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9EmtdD3rRT2B6ECD0y-yT69RvJoLIIGaEhreD0KR_nA&s=10',
        'pic2': 'https://images.unsplash.com/photo-1580060860978-d479ebf95a53?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
    }
]



def Asia(request):
    context = {'data':data}
    return render(request, 'asia.html', context)

def Europe(request):
    context2 = {'data2':data2}
    return render(request, 'europe.html', context2)

def Australia(request):
    context3 = {'data3':data3}
    return render(request, 'australia.html', context3)

def Canada(request):
    context4 = {'data4':data4}
    return render(request, 'canada.html', context4)

def Africa(request):
    context5 = {'data5':data5}
    return render(request, 'africa.html', {'data5':data5})

def about(request):
    return render(request, 'about.html')

def read(request, id):

    all_data = data + data2 + data3 + data4 + data5

    for i in all_data:
        if i['id'] == int(id):
            return render(request, 'read.html', {'data': i})

