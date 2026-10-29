| ENCAPSULAMENTO |

Visa manter a integridade do sistema, protegendo o estado 
interno do objeto contra interferência externa não regulamentada.
Envolvemos ele em uma "cápsula" que deixa exposto apenas o que é acessível.

Principais Vantagens:
   - Segurança e controle
   - Facilidade de manutenção
   - Flexibilidade e reutilização
   - Redução de efeitos colaterais

   | VISIBILIDADE |

Existem 3 tipos de visibilidade para atributos em linguagens POO:
   - public:      +
   - protected:   #
   - private:     -

   class A() <-- classe mãe
   + atributo1  <--- public:    acessível em todo o código ---------------------------------------->||| não tem underlines ou símbolos para deixar público  
   # _atributo2  <--- protected: acesseível somente para classe mãe e filhas, mas não no main ----->||| para deixar protegido use 1 underline no atribut  
   - __atributo3  <--- private:   acessível somente para classe mãe  ------------------------------>||| para deixar o atributo privado, use 2 underlines no atributo  
   |    |________
   |             |
class B()    class C() <-- classes filhas


   main()
      a = A()
      b = B()
      c = C()