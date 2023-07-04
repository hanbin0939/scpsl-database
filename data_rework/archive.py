import discord

class archive_view(discord.ui.View):
    @discord.ui.select(
        placeholder="choose the Old Data",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(
                label="Ebsillon-11",
                value="1",
                description="old E-11 model (0.1.0 ~ 6.0.0)"
            ),
            discord.SelectOption(
                label="M1911 Pistol",
                value="2",
                description="old pistol (0.1.0 ~ 6.0.0)"
            ),
            discord.SelectOption(
                label="SBX-7 Pistol",
                value="3",
                description="MTF Guard Standard Pistol (Beta [2017-08-23] ~ 6.0.0)"
            ),
            discord.SelectOption(
                label="Skorpion",
                value="4",
                description="SMG gun"
            ),
            discord.SelectOption(
                label="Logicer",
                value="5",
                description="0.1.0 ~ 6.0.0"
            ),
            discord.SelectOption(
                label="Micro .H.I.D",
                value="6",
                description="(Beta [2017-08-23] ~ 6.0.0)"
            ),
            discord.SelectOption(
                label="E-11-SR",
                value="7",
                description="6.0.0 ~ 7.2.0"
            ),
            discord.SelectOption(
                label="E-11"
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "1":
            embed = discord.Embed(description="""```ansi\n[2;34m[1;34m█ Ebsillon - 11 Fusion Rife █[0m[2;34m[0m[2;34m[1;34m[0m[2;34m[0m```
            Standard Nine-Tailed Fox equipment.
            ```ansi\n[2;34m[1;34m█ add in █[0m[2;34m[0m[2;34m[1;34m[0m[2;34m[0m\n```• 09/12-18/2017
            ```ansi\n[2;34m[1;34m█ remove in █[0m[2;34m[0m\n```• 6.0.0 (First Weapon Rework)
            ```ansi\n[2;34m[1;34mDescription[0m[2;34m[0m\n```• E-11 Standard Rifle is the second iteration of MTF-E11-SR firearm in SCP:SL. It was a heavy rifle with high recoil. It used SCP Fusion Ammo, like any other fusion firearm. This is the original model made for SCP:SL.
            ```ansi\n[2;34m[1;34m█ more information old wiki █[0m[2;34m[0m\n```"The rifle itself is made of steel, and the main part is painted with dark blue paint... The total length of the weapon (Counting from the butt to the muzzle) is 847 mm, and its weight with a loaded magazine is 4 kilograms."
            ```ansi\n[2;34m[1;34m█ Remove Reason █[0m[2;34m[0m\n```Rework of game weapons and their transition from futuristic to modern weapons.
            ```ansi\n[1;2m[1;34mStatus[0m[0m\n```• 탄약 - 40\n • 데미지 - 18 ; 헤드샷 - 54\n • 탄약 - SFA\n • 반동 - 60\n • 발사속도 - 420\n • 제장전시간 - 4.8s
            """,color=0x268bd2)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/5/59/OlderE11SRIcon.png")
            embed.set_image(url='https://media.discordapp.net/attachments/853704746166911056/1086757924224909353/MoreFusion.png?width=1177&height=662')
            embed2 = discord.Embed(description="```ansi\n[2;34m[1;34mconcept art[0m[2;34m[0m\n```",color=0x268bd2)
            embed2.set_thumbnail(url="https://media.discordapp.net/attachments/845744801600372766/922532541548871750/Epsilon_11_Wiki.png")
            embed2.set_image(url="https://images-ext-2.discordapp.net/external/gZbKa41y1C4omSEPhe_CQkjqUaALCg91Qk0taZ6ucFI/https/images-ext-2.discordapp.net/external/vMAFmSRuhpbH79MZBHBLNc9HBFEstJ6Ud6_NQ0clT5s/https/i.imgur.com/BupBP03.png")
            embed2.set_footer(text="Image of old game WIKI")
            await interaction.response.edit_message(embeds=[embed,embed2])
        if select.values[0] == "2":
            embed = discord.Embed(description="""```ansi\n[2;34m[1;34m█ M1911 Pistol █[0m[2;34m[0m\n```Basic personal defense weapon.
            ```ansi\n[2;34m[1;34m█ Add in █[0m[2;34m[0m\n```• ɑlpha_Testing [2017-06-28]
            ```ansi\n[2;34m[1;34m█ Remove in █[0m[2;34m[0m\n```• 6.0.0
            ```ansi\n[2;34m[1;34mStatus[0m[2;34m[0m\n``` • 탄약 - 12\n • 데미지 - (몸) 21 ; (머리) 61\n • Ammo Type - PAT\n • 발사속도 - 180\n • 장전시간 - 3.3
            ```ansi\n[2;34m[1;34mdescription\n```The M1911 pistol, named Colt 1911 in reality, is the weakest weapon in the game due to low accuracy, reload speed and magazine capacity. There are only 2 of these pistols around the facility, and none of the playable classes spawn with it. The gun itself is the first ever weapon added to the game, it was added back when exiting Light Containment Zone was impossible altogether.
Fun fact! During the shooting tutorial, the narrator says the following phrase in regards to this weapon: "-This is the shittiest weapon in the game..."
            """,color=0x268bd2)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/3/3c/Pistol1911Icon.png")
            embed.set_image(url="https://media.discordapp.net/attachments/845744801600372766/935899367976615947/Colt_1911.png?width=1243&height=676")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "3":
            embed = discord.Embed(description="""```ansi\n[2;34m[1;34m█ SBX - 7 █[0m[2;34m[0m\n```Fusion-ammo pistol.
            ```ansi\n[2;34m[1;34m█ add in █[0m[2;34m[0m\n``` • 0.1.0
            ```ansi\n[2;34m[1;34m█ Remove in █[0m[2;34m[0m``` • 6.0.0
            ```ansi\n[2;34m[1;34mStatus[0m[2;34m[0m\n``` • 탄약수 - 10\n • Damage - (Body) 21 ; (Head) 6\n • Ammo Type - SFA\n • 발사속도 - 120\n • 제장전시간 - 3.4/s
            ```ansi\n[2;34m[1;34mdescription\n```The first pistol that appeared in the game uses the same fusion system as the Epsilon-11 rifle. The recoil while firing without a scope was extremely high, preventing accurate fire. In addition, low rate of fire, low damage and strong recoil, coupled with a small 10-round magazine, makes this pistol one of the weakest weapons in the game. During the development period, the pistol changed its name 3 times. Starting as FB-55, continuing as SC-Pistol and ending as SBX-7. Standardly issued to each MTF Cadet (Guard). Like the Epsilon-11, it had a scope, but unlike the rifle named above, it had a red color.
            """,color=0x268bd2)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/a/a5/SBX7PistolIcon.png")
            embed.set_image(url="https://images-ext-1.discordapp.net/external/VIr_SDiJcDtDAGmpcH_G0GJ0iiAuqzSPyauGrn_NFB4/https/media.discordapp.net/attachments/638372158715723818/865591398601719828/SBXeevee.png?width=1202&height=676")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "4":
            embed = discord.Embed(description="""```ansi\n[2;34m[1;34m█ Skorpion █[0m[2;34m[0m\n```SMG type-weapon
            ```ansi\n[2;34m[1;34m█ add in █[0m[2;34m[0m\n``` • 08/20/2017
            ```ansi\n[2;34m[1;34m█ remove in █[0m[2;34m[0m\n``` • 6.0.0
            ```ansi\n[2;34m[1;34m█ status █[0m[2;34m[0m\n[2;31m[1;31m▮ No Data ▮[0m[2;31m[0m\n```""",color=0x268bd2)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/4/4e/SkorpionIcon.png")
            embed.set_image(url="https://media.discordapp.net/attachments/845744801600372766/934480412229644298/Scorpion.png?width=1440&height=463")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "5":
            embed = discord.Embed(description="""```ansi\n[2;32m[1;32m█ Logicer █[0m[2;32m[0m\n```Standard C.I. equipment
            ```ansi\n[2;32m[1;32m█ add in █[0m[2;32m[0m\n```• June 2017

            ```ansi\n[2;32m[1;32m█ status █[0m[2;32m[0m\n```• 탄약수 : 100\n • damage - (Body)16;(Head)48\n • ammo type : RAT\n • 발사속도 : 3600\n • 장전시간 : 8.3/s
            """,color=0x859900)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/9/9a/OldestLogicerIcon.png/507px-OldestLogicerIcon.png")
            embed.set_image(url="https://media.discordapp.net/attachments/845744801600372766/950740080895598602/Logicer.png?width=1440&height=504")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "6":
            embed = discord.Embed()