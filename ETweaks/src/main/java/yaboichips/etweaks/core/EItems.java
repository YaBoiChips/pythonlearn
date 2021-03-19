package yaboichips.etweaks.core;

import net.minecraft.item.*;
import net.minecraft.util.ResourceLocation;
import yaboichips.etweaks.ETweaks;
import yaboichips.etweaks.common.items.misc.ReusableEnderPearl;
import yaboichips.etweaks.common.items.misc.VillagerTrapItem;

import java.util.ArrayList;
import java.util.List;

public class EItems {

    public static List<Item> items = new ArrayList<>();

    public static final ItemGroup TWEAKS_TAB = new ItemGroup(ETweaks.MOD_ID) {
        @Override
        public ItemStack createIcon() {
            return new ItemStack(Items.CHAIN_COMMAND_BLOCK);
        }
        @Override
        public boolean hasScrollbar() {
            return true;
        }
        @Override
        public ResourceLocation getBackgroundImage() {
            return new ResourceLocation("minecraft", "textures/gui/container/creative_inventory/tab_items.png");
        }
    };

    //misc
    public static final Item VILLAGER_TRAP = createItem(new VillagerTrapItem(new Item.Properties().group(TWEAKS_TAB)), "villager_trap");
    public static final Item REUSEABLE_ENDER_PEARL = createItem(new ReusableEnderPearl(new Item.Properties().group(TWEAKS_TAB)), "reusable_ender_pearl");
    public static final Item REDDIT_SILVER = createItem(new Item(new Item.Properties().group(TWEAKS_TAB)), "reddit_silver");
    public static final Item REDDIT_GOLD = createItem(new Item(new Item.Properties().group(TWEAKS_TAB)), "reddit_gold");

    //food
    public static final Item PICKLE = createItem(new Item(new Item.Properties().food(EFoods.PICKLE).group(TWEAKS_TAB)), "pickle");
    public static final Item SUPERMEAL = createItem(new Item(new Item.Properties().food(EFoods.SUPERMEAL).group(TWEAKS_TAB)), "supermeal");

    public static Item createItem(Item item, String id) {
        return createItem(item, ETweaks.createResource(id));
    }

    public static Item createItem(Item item, ResourceLocation id) {
        if (id != null && !id.equals(new ResourceLocation("minecraft:air"))) {
            item.setRegistryName(id);

            items.add(item);

            return item;
        } else return null;
    }

    public static void init() {
    }
}
