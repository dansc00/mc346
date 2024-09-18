
-- recebe chave e contador em formato de lista de tuplas, incrementa tupla que possui a chave passada
incrementar chave contador = map (\x -> if (fst x == chave) then (chave, (snd x)+1) else (fst x, snd x)) contador

agruparChaves chave contador
    | (valChave == valX) || (valChave == valX+32) = (chave,contador) : incrementar chave xs 
    | otherwise = incrementar chave xs
    where
        valChave = fromEnum chave -- valor inteiro do caracter pela tabela ASCII
        valX = fromEnum x

-- constrói contador em formato de lista de tuplas, com uma ocorrência de cada chave
construirContador [] = []
construirContador (x:xs) = (x,1) : construirContador xs
 
letraMaisComum string = 
    where
        listaFiltrada = filter (\ x -> (x >= 'a' && x <= 'z') || (x >= 'A' && x <= 'Z')) string -- string com apenas letras
        contador = construirContador listaFiltrada 