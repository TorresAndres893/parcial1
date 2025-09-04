import org.antlr.v4.runtime.*;

public class Euler {
    public static void main(String[] args) {
        String input = "exp(x, 10)";  // primeros 10 términos
        double xVal = 1.0;            // valor de x

        GramaLexer lexer = new GramaLexer(CharStreams.fromString(input));
        GramaParser parser = new GramaParser(new CommonTokenStream(lexer));
        GramaParser.ExprContext tree = parser.expr();

        EvalVisitor visitor = new EvalVisitor(xVal);
        double result = visitor.visit(tree);

        System.out.println("Aprox e^" + xVal + " con 10 términos = " + result);
    }
}
