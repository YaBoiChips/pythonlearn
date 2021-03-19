package chess.game;

import chess.dice.Die;

public abstract class Tile {

    int tileCoordinate;

    public Tile(int tileCoordinate){
        this.tileCoordinate = tileCoordinate;
    }

    public abstract boolean hasDie();

    public abstract Die getDie();

    public static final class EmptyTile extends Tile{

        EmptyTile(int coordinate) {
            super(coordinate);
        }

        @Override
        public boolean hasDie() {
            return false;
        }

        @Override
        public Die getDie() {
            return null;
        }
    }

    public static final class OccupiedTile extends Tile{

        Die dieOnTile;

        public OccupiedTile(int tileCoordinate, Die dieOnTile) {
            super(tileCoordinate);
            this.dieOnTile = dieOnTile;
        }

        @Override
        public boolean hasDie() {
            return true;
        }

        @Override
        public Die getDie() {
            return this.dieOnTile;
        }
    }
}
