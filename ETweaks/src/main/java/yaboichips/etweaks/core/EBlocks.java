package yaboichips.etweaks.core;

import net.minecraft.block.AbstractBlock;
import net.minecraft.block.Block;
import net.minecraft.block.EndRodBlock;
import net.minecraft.block.material.Material;
import yaboichips.etweaks.ETweaks;

import javax.annotation.Nonnull;
import java.util.ArrayList;
import java.util.List;

public class EBlocks {

    public static List<Block> blocks = new ArrayList<>();

    public static final Block RED_END_ROD = registerBlock("red_end_rod", new EndRodBlock(AbstractBlock.Properties.create(Material.MISCELLANEOUS).zeroHardnessAndResistance().setLightLevel((state) -> 14)));
    public static final Block BLUE_END_ROD = registerBlock("blue_end_rod", new EndRodBlock(AbstractBlock.Properties.create(Material.MISCELLANEOUS).zeroHardnessAndResistance().setLightLevel((state) -> 14)));
    public static final Block GREEN_END_ROD = registerBlock("green_end_rod", new EndRodBlock(AbstractBlock.Properties.create(Material.MISCELLANEOUS).zeroHardnessAndResistance().setLightLevel((state) -> 14)));
    public static final Block YELLOW_END_ROD = registerBlock("yellow_end_rod", new EndRodBlock(AbstractBlock.Properties.create(Material.MISCELLANEOUS).zeroHardnessAndResistance().setLightLevel((state) -> 14)));
    public static final Block ORANGE_END_ROD = registerBlock("orange_end_rod", new EndRodBlock(AbstractBlock.Properties.create(Material.MISCELLANEOUS).zeroHardnessAndResistance().setLightLevel((state) -> 14)));
    public static final Block PINK_END_ROD = registerBlock("pink_end_rod", new EndRodBlock(AbstractBlock.Properties.create(Material.MISCELLANEOUS).zeroHardnessAndResistance().setLightLevel((state) -> 14)));
    public static final Block BLACK_END_ROD = registerBlock("black_end_rod", new EndRodBlock(AbstractBlock.Properties.create(Material.MISCELLANEOUS).zeroHardnessAndResistance().setLightLevel((state) -> 14)));
    public static final Block PURPLE_END_ROD = registerBlock("purple_end_rod", new EndRodBlock(AbstractBlock.Properties.create(Material.MISCELLANEOUS).zeroHardnessAndResistance().setLightLevel((state) -> 14)));
    public static final Block LIGHT_BLUE_END_ROD = registerBlock("light_blue_end_rod", new EndRodBlock(AbstractBlock.Properties.create(Material.MISCELLANEOUS).zeroHardnessAndResistance().setLightLevel((state) -> 14)));



    static @Nonnull
    <T extends Block> T registerBlock(String id, @Nonnull T block) {
        block.setRegistryName(ETweaks.createResource(id));

        blocks.add(block);

        return block;
    }

    public static void init() {
    }
}
