public class EvalVisitor extends GramaBaseVisitor<Double> {

    private final double x; // valor de x

    public EvalVisitor(double x) {
        this.x = x;
    }

    @Override
    public Double visitExpCall(GramaParser.ExpCallContext ctx) {
        // Ignoramos el ID porque asumimos que siempre es "x"
        int n = Integer.parseInt(ctx.INT().getText()); // número de términos
        double sum = 0.0;
        for (int k = 0; k <= n; k++) {
            sum += Math.pow(x, k) / factorial(k);
        }
        return sum;
    }

    private double factorial(int n) {
        double f = 1.0;
        for (int i = 2; i <= n; i++) {
            f *= i;
        }
        return f;
    }
}
