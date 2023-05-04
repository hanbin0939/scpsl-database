import discord
class scp_items(discord.ui.View):
    @discord.ui.select(
        placeholder = "Choose a Class!",
        min_values = 1,
        max_values = 1, 
        options = [ 
            discord.SelectOption(
                label="SCP 018",
                value = "1",
                description="super ball"
            ),
            discord.SelectOption(
                label="SCP 207",
                value="2",
                description="coka cola"
            ),
            discord.SelectOption(
                label="SCP 244",
                value="3",
                description="ice Jar"
            ),
            discord.SelectOption(
                label="SCP 268",
                value="4",
                description="쓰면 투명해지는 모자"
            ),
            discord.SelectOption(
                label="SCP 500",
                value="5",
                description="만병통치약"
            ),
            discord.SelectOption(
                label="Anti SCP 207",
                value="6",
                description="ANTI SCP 207"
            ),
            discord.SelectOption(
                label="SCP 1853",
                value="7",
                description="상호작용 속도를 높여줍니다."
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "1":
            embed = discord.Embed(title="SCP018",description="super ball")
            embed.set_author(name='SCPitem',icon_url='https://hub.scpslgame.com/images/thumb/4/44/NEWSCPCAT.png/180px-NEWSCPCAT.png')
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/b/b3/SCP018Icon.png/180px-SCP018Icon.png")
            embed.set_footer(text="튕기면 튕길수록 강해지는 공")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "2":
            embed = discord.Embed(title="SCP207",url="https://en.scpslgame.com/index.php?title=SCP-207",color=0xff0000)
            embed.set_author(name='SCPitem',icon_url='https://hub.scpslgame.com/images/thumb/8/8b/CATEFFECT.png/61px-CATEFFECT.png')
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/d/dd/UpdatedSCP207Icon.png/300px-UpdatedSCP207Icon.png')
            embed.add_field(name='LV1',value='>>>207 X1 : 6.48m/sec ,-1HP.s',inline=False)
            embed.add_field(name='LV2',value='>>>207 X2 : 7.45m/sec , -1.5hp.s',inline=True)
            embed.add_field(name='LV3',value='>>>207 X3 : 8.1m/sec ,-2.5HP.s',inline=False)
            embed.add_field(name='LV4',value='>>>207 X4 : 8.42m/sec -4HP.s',inline=True)
            embed.set_footer(icon_url='https://hub.scpslgame.com/images/thumb/4/44/NEWSCPCAT.png/180px-NEWSCPCAT.png')
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "3":
            embed = discord.Embed(title='SCP244',url="https://en.scpslgame.com/index.php?title=SCP-244",description='An ancient vase, freezing to the touch.\nCreates a large cloud of icy fog when placed',color=0x85c2de)
            embed.set_author(name='SCPitem',icon_url='https://hub.scpslgame.com/images/thumb/4/44/NEWSCPCAT.png/180px-NEWSCPCAT.png')
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/3/30/SCP244BIcon.png/300px-SCP244BIcon.png')
            embed.set_footer(text='SCP item',icon_url='https://hub.scpslgame.com/images/thumb/3/32/SCP244AIcon.png/300px-SCP244AIcon.png')
            embed.add_field(name="SCP-049-2",value='공격속도 쿨다운 + 2 & 공격속도 감소 & 스팩 감소',inline=True)
            embed.add_field(name="SCP-096",value="폭주 __불가능__",inline=True)
            embed.add_field(name="SCP-106",value="공격 쿨다온 속도 증가",inline=True)
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "4":
            embed = discord.Embed(title="SCP-268",description="빵모자",color=0xFFD500)
            embed.set_author(name='SCPitem',icon_url='https://hub.scpslgame.com/images/thumb/4/44/NEWSCPCAT.png/180px-NEWSCPCAT.png')
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/e/e8/UpdatedSCP268Icon.png/375px-UpdatedSCP268Icon.png")
            embed.set_footer(text="상호작용이 없을경우 최대 15초동안 투명상태를 유지할수 있습니다!")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "5":
            embed = discord.Embed(title="SCP500",description="만병통치약",color=0xff0000)
            embed.set_author(name='SCPitem',icon_url='https://hub.scpslgame.com/images/thumb/4/44/NEWSCPCAT.png/180px-NEWSCPCAT.png')
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/a/ac/SCP500Icon.png/375px-SCP500Icon.png")
            embed.add_field(name="기능1",value="상대방을 완전 회복합니다.")
            embed.add_field(name="기능2",value="20초동안 200hp 추가회복")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "6":
            embed = discord.Embed(title="Anti SCP207")
            embed.set_author(name='SCPitem',icon_url='https://hub.scpslgame.com/images/thumb/8/8b/CATEFFECT.png/61px-CATEFFECT.png')
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/912017883788357662/1098038788439154769/SCP207Icon_1.png")
            embed.set_footer(text="이동속도를 줄이는 대신 hp 회복\nSCP 207 + Anti SCP207 = Pink Candy")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "7":
            embed = discord.Embed(title="SCP 1853",description="기동성 강화제",color=0x008000)
            embed.set_author(name='SCPitem',icon_url='https://hub.scpslgame.com/images/thumb/4/44/NEWSCPCAT.png/180px-NEWSCPCAT.png')
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/d/d8/SCP1853Icon.png/300px-SCP1853Icon.png")
            embed.add_field(name="option 1",value="Picking up items is faster by 60%.")
            embed.add_field(name="option 2",value="ADS Inaccuracy reduced by 30%.")
            embed.add_field(name="option 3",value="25% reduction in weapon recoil.")
            embed.add_field(name="option 4",value="25% reduction in weapon reload/unload time.")
            embed.add_field(name="option 5",value="Entering/Exiting ADS is faster by 20%.")
            embed.add_field(name="option 6",value="20% reducation in draw & usage time for certain items")
            await interaction.response.edit_message(embed=embed)
